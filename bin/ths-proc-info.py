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


for prinfo in psutil.process_iter():
    try:
        cmd_first = prinfo.cmdline()[0]
        if re.match('.*php-fpm: pool.+', cmd_first):
            p_data_list = []
            pool = cmd_first.split()[-1]
            print(prinfo.memory_info()["rss"])
    except (psutil.NoSuchProcess, psutil.AccessDenied, IndexError):
        pass
