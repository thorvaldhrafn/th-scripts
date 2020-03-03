# from __future__ import print_function

import psutil
import re
import os
import sys

# for proc in psutil.process_iter():
#     try:
#         processName = proc.name()
#         processID = proc.pid
#         print(processName , ' ::: ', processID)
#     except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#         pass

# pool_dir = "/etc/php-fpm.d/"
# pool_conf_flist = os.listdir(pool_dir)
# pool_conf_list = list()
#
# for i in pool_conf_flist:
#     if re.match('.+\.conf', i):
#         pool_conf_list.append(i)
#


def p_mem_rss_full(pname, p_mem_rss):
    global proc_mem_list
    try:
        p_mem_rss_old = proc_mem_list[pname]['rss']
        p_mem_rss_new = p_mem_rss_old + p_mem_rss
        proc_mem_list[pname]['rss'] = p_mem_rss_new
    except KeyError:
        proc_mem_list[pname]['rss'] = p_mem_rss

proc_mem_list = {}

for prinfo in psutil.process_iter():
    try:
        cmd_first = prinfo.cmdline()[0]
        if re.match('.*php-fpm: pool.+', cmd_first):
            p_data_list = []
            pool = cmd_first.split()[-1]
            p_mem_data = prinfo.memory_info()
            p_mem_rss = p_mem_data.rss
    except (psutil.NoSuchProcess, psutil.AccessDenied, IndexError):
        pass

for key in proc_mem_list.keys():
    print(key, proc_mem_list[key]['rss'])
