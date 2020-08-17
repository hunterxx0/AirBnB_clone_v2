#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive.
"""
from datetime import datetime
from fabric.api import *
from os.path import exists
env.hosts = ['35.231.7.140', '35.227.72.212']


def do_pack():
    """ """
    local('mkdir -p versions')
    name = 'versions/web_static_{}\
.tgz'.format(datetime.now().strftime("%Y%m%d%H%M%S"))
    arch = local('tar -vczf {} web_static'.format(name))
    if arch.failed:
        return None
    else:
        return (name)


def do_deploy(archive_path):
    """ Distributes an archive to your web servers """
    if not exists(archive_path):
        return False
    name = archive_path.split('/')[-1]
    put(archive_path, '/tmp/')
    src = '/data/web_static/releases/' + name.split('.')[0]
    run('mkdir -p {}'.format(src))
    run('tar -xzf /tmp/{} -C {}'.format(name, src))
    run('rm /tmp/{}'.format(name))
    run('mv {}/web_static/* {}'.format(src, src))
    run('rm -rf /data/web_static/current')
    run('rm -rf {}/web_static'.format(src))
    run('ln -s {} /data/web_static/current'.format(src))
    return True


def deploy():
    """ creates and distributes an archive to your web servers """
    full = do_pack()
    if full:
        return do_deploy(full)
    else:
        return False
