
"""Fabric script that distributes an archive to my web servers.

Uses the function do_deploy to:
"""

import os.path
from fabric.api import local, put, run, env

env.hosts = ['54.144.146.11', '54.90.48.124']


def do_deploy(archive_path):
    """Distributes an archive to specific host servers.

    Returns False if the file at the path archive_path doesn’t exist
    The script should take the following steps:

    Upload the archive to the /tmp/ directory of the web server
    Uncompress the archive to the folder
        /data/web_static/releases/<archive filename without extension>
        on the web server
    Delete the archive from the web server
    Delete the symbolic link /data/web_static/current from the web server
    Create a new the symbolic link /data/web_static/current on the web server,
        linked to the new version of your code
        (/data/web_static/releases/<archive filename without extension>)

    All remote commands must be executed on your both web servers
        (using env.hosts = ['<IP web-01>', 'IP web-02'] variable in my script)
    Returns True if all operations have been done correctly,
        otherwise returns False
    """

    if archive_path:
        found = os.path.exists(f'{archive_path}')
        file_name = f'{archive_path}'.split('/')[1]
        file_name_without_extension = file_name.replace('.tgz', '')

    if found:
        task = put(f'{archive_path}', '/tmp')
    else:
        return False

    if task.succeeded:
        task = run('mkdir -p /data/web_static/releases/' +
                   f'{file_name_without_extension}')
    if task.succeeded:
        task = run(f'tar -xzf /tmp/{file_name} -C ' +
                   f'/data/web_static/releases/{file_name_without_extension}')
    if task.succeeded:
        task = run(f'rm /tmp/{file_name}')
    if task.succeeded:
        task = run('mv /data/web_static/releases/' +
                   f'{file_name_without_extension}/web_static/* ' +
                   f'/data/web_static/releases/{file_name_without_extension}/')
    if task.succeeded:
        task = run('rm -rf /data/web_static/releases/' +
                   f'{file_name_without_extension}/web_static')
    if task.succeeded:
        task = run('unlink /data/web_static/current')
    if task.succeeded:
        task = run('ln -sf /data/web_static/releases/' +
                   f'{file_name_without_extension} /data/web_static/current')
        return True

    return False
