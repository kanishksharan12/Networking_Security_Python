#!/usr/bin/python
__author__ = 'Kanishk Sharan'

import os

rootdir = "C:\\$Recycle.Bin"
for curr, dirs, files in os.walk(rootdir):
    for f in files:
        path = "%s/%s" % (curr, f)
        print (path)
