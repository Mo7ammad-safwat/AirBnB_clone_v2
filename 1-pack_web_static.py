#!/usr/bin/python3

"""Generates a .tgz archive from the contents of the web_static folder
    of your AirBnB Clone repo, using the function do_pack
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """Function to generate a .tgz archive
    """
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = f"versions/web_static_{date_time}.tgz"
    cmd = f"tar -cvzf {archive_path} web_static"

    if not os.path.exists("versions"):
        os.makedirs("versions")

    if local(cmd).failed is True:
        return (None)
    return (archive_path)
