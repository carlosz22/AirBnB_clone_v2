#!/usr/bin/python3
"""
Fabric script to generate a .tgz from web_static folder
"""
from fabric.api import *
import datetime


def do_pack():
    """
    Compress the content of web_static folder in a .tgz
    """
    now = datetime.datetime.now()
    str_time = now.strftime("%Y%m%d%H%M%S")
    file_name = "web_static_{}".format(str_time)
    local("mkdir -p versions")
    status_f = local("tar -cvzf versions/{}.tgz web_static".format(file_name))

    if status_f.succeeded:
        return "versions/{}.tzg".format(file_name)
    else:
        return None
