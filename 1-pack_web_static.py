#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive.
"""
from datetime import datetime
from fabric.api import local


def do_pack():
    """ Fabric script that generates a .tgz archive """
    local('mkdir -p versions')
    name = 'versions/web_static_{}\
.tgz'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    arch = local('tar -vczf {} web_static'.format(name))
    if arch.failed:
        return None
    else:
        return (name)
