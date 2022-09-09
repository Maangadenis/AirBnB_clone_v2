#!/usr/bin/python3
""" 0x03. AirBnB clone - Deploy static, task 2. Deploy archive!
"""
from fabric.api import env, put, run
from os import path

env.hosts = ['35.196.49.136', '34.74.70.223']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """ Distributes a .tgz archive from the contents of `web_static/` in AirBnB
    clone repo to the web servers

    Retruns:
        (bool): `True` if all operations successful, `False` otherwise
    """
    if not path.exists(archive_path) or archive_path is None:
        return False

    f_name = path.basename(archive_path)
    d_name = f_name.split('.')[0]

    put(local_path=archive_path, remote_path='/tmp/')
    run('mkdir -p /data/web_static/releases/{}/'.format(d_name))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(
        f_name, d_name))
    run('rm /tmp/{}'.format(f_name))
    run('mv /data/web_static/releases/{}/web_static/* '.format(d_name) +
        '/data/web_static/releases/{}/'.format(d_name))
    run('rm -rf /data/web_static/releases/{}/web_static'.format(d_name))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{}/ /data/web_static/current'.format(
        d_name))

    return True
