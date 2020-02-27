from __future__ import print_function

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
        if re.match('.*php-fpm: pool.+', prinfo.cmdline()[0]):
            print(prinfo.cmdline())
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass
