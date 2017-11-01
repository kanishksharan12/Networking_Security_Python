#!/usr/bin/python
__author__ = 'Kanishk Sharan'

import psutil

l = psutil.get_process_list()

for proc in l:
    print(proc)
    print(proc.name())
    if (proc.name() == "Python"):
        print(proc.get_memory_maps())
