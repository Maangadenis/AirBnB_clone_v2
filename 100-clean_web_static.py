#!/usr/bin/python3
""" 0x03. AirBnB clone - Deploy static, task 4. Keep it clean!
"""
from fabric.api import env, run, local

env.hosts = ['35.196.49.136', '34.74.70.223']
env.user = 'ubuntu'


def do_clean(number=0):
    """ Deletes out-of-date .tgz archives of `web_static/`, both local and
    remote, created by `do_pack`.

    Args:
       (str): number of archives, including the most recent, to keep. If 0 or
            1, only the most recent is kept.

    """
    number = eval(number)
    if number == 0:
        number = 1
    # local removal of tgz archives
    pipe = ' '.join(('ls -t versions/ | tail -n +{:d} |'.format(number+1),
                     'sed -e "s/^/versions\//" |',
                     'xargs rm -rf'))
    local(pipe)

    # run on server to remove outdated directories in web_static/releases/
    pipe = ' '.join(('ls -t /data/web_static/releases/ |',
                     'sed -e "/test/d" |',
                     'tail -n +{:d} |'.format(number+1),
                     'sed -e "s/^/\/data\/web_static\/releases\//" |',
                     'xargs rm -rf'))
    run(pipe)
