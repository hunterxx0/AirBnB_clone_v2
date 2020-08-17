#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive.
"""
from datetime import datetime
from fabric.api import *
from os import walk
env.hosts = ['35.231.7.140', '35.227.72.212']


def do_clean(number=0):
    """ deletes out-of-date archives """
    if int(number) == 0:
        number = 1
    else:
        number = int(number)
    f = []
    for (dirpath, dirnames, filenames) in walk("./versions/"):
        f.extend(filenames)
        break
    f.sort()
    for i in range(number):
        f.pop()
    with lcd("./versions/"):
        for i in f:
                local("rm -rf {}".format(i))
    with cd("/data/web_static/releases"):
        h = run("ls -rt").split()
        z = [i for i in h if "_static_" in i]
        for i in range(number):
            z.pop()
        for i in z:
            local("rm -rf {}".format(i))
