#!/usr/bin/python3
"""Fab file to generate a .tgz archive file.

The contents of the "web_static" folder from my AirBnB clone repo are used
for the archive file.
Details:
    - All files in the folder web_static is added to the final archive.
    - All archives are stored in the folder versions
        (the function creates this folder if it doesn’t exist).
    - The name of the created archive will be:
        web_static_<year><month><day><hour><minute><second>.tgz
    - The function do_pack must return the archive path if the archive
        has been correctly generated. Otherwise, it will return None.
"""

from fabric.api import local
from datetime import datetime
from os.path import exists


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
