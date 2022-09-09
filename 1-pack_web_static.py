#!/usr/bin/python3
""" 0x03. AirBnB clone - Deploy static, task 1. Compress before sending
"""
from fabric.api import local, env
from os import path, makedirs, listdir
from datetime import datetime


def do_pack():
    """ Generates a .tgz archive from the contents `web_static/` in AirBnB clone
    repo.

    Retruns:
        (str): full path from current directory to `.tgz` archive created in
    `versions/`, or `None` on failure
    """
    if not path.isdir("./versions"):
        makedirs("./versions")

    now = datetime.now().strftime('%Y%m%d%H%M%S')
    local('tar -cvzf versions/web_static_{}.tgz web_static/'.format(now))

    files = listdir("./versions")
    paths = [path.join("./versions", base_name) for base_name in files]
    if len(paths) == 0:
        return None
    return max(paths, key=path.getctime)
