#!/usr/bin/python3
"""Fab script that creates and distributes an archive using other fab scripts
"""

from fabric.api import env
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy
env.hosts = ['54.144.146.11', '54.90.48.124']

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

    success = False
    archive_path = do_pack()

    if archive_path:
        success = do_deploy(archive_path)

    return success
