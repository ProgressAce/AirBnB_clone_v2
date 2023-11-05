#!/usr/bin/python3
"""Fab script that creates and distributes an archive using other fab scripts
"""

from fabric.api import local, env, put, run
from datetime import datetime
from os.path import exists

env.hosts = ['54.144.146.11', '54.90.48.124']


def do_pack():
    """Generates the .tgz archive file.
    """

    found = False
    now = datetime.now()
    date_format = '{}{:02d}{:02d}{:02d}{:02d}{:02d}'.format(
                   now.year, now.month, now.day,
                   now.hour, now.minute, now.second)

    local('mkdir -p versions')
    status = local(f'tar -vczf versions/web_static_{date_format}.tgz ' +
                   'web_static/')

    if status.succeeded:
        found = exists(f'versions/web_static_{date_format}.tgz')

    if found:
        return f'versions/web_static_{date_format}.tgz'
    else:
        return None


def do_deploy(archive_path):
    """Distributes an archive to specific host servers.

    Returns True if all operations have been done correctly,
        otherwise returns False
    """

    if not exists(archive_path):
        return False

    file_name = f'{archive_path}'.split('/')[1]
    file_name_without_extension = file_name.replace('.tgz', '')

    try:
        put(f'{archive_path}', '/tmp')
        run('mkdir -p /data/web_static/releases/' +
            f'{file_name_without_extension}')
        run(f'tar -xzf /tmp/{file_name} -C ' +
            f'/data/web_static/releases/{file_name_without_extension}')
        run(f'rm /tmp/{file_name}')
        run('mv /data/web_static/releases/' +
            f'{file_name_without_extension}/web_static/* ' +
            f'/data/web_static/releases/{file_name_without_extension}/')
        run('rm -rf /data/web_static/releases/' +
            f'{file_name_without_extension}/web_static')
        run('rm -rf /data/web_static/current')
        run('ln -sf /data/web_static/releases/' +
            f'{file_name_without_extension} /data/web_static/current')
        return True
    except Exception:
        return False


def deploy():
    """Creates and distributes an archive file to the spceified host servers.

    The script should take the following steps:
    1.Call the do_pack() function and store the path of the created archive.
    2.Return False if no archive has been created.
    3.Call the do_deploy(archive_path) function, using the new path
        of the new archive.
    4.Return the return value of do_deploy.

    All remote commands must be executed on both of web your servers
        (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in my script)
    This script deploya to servers: xx-web-01 and xx-web-02
    """

    archive_path = do_pack()
    if archive_path is None:
        return False

    return do_deploy(archive_path)
