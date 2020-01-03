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
    str_time = now.strtime("%Y%m%d%H%M%S")
    file_name = "web_static{}".format(str_time)
    run("mkdir versions")
    status_file = run("tar -cvzf versions/{}.tgz web_static".format(file_name))

    if status_file == 0:
        return "versions/{}.tzg".format(file_name)
    else:
        return None
