#!/usr/bin/python3

"""Script (based on the file 3-deploy_web_static.py) that deletes
    out-of-date archives, using the function do_clean
"""
from fabric.api import local, run, env
import subprocess

env.hosts = [
            '54.164.149.90',
            '18.234.107.151'
        ]

env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"
repeate = None


def del_versions(versions, number=0, loc=None):
    """Delete files from versions
    """
    versions_split = versions.strip().split()
    versions_split.sort(reverse=True)  # Sort descending to easily keep the newest
    if number > 0:
        versions_to_delete = versions_split[number:]  # Exclude the 'number' of recent files
    else:
        versions_to_delete = versions_split[1:]  # Default to keeping the newest file

    for ver in versions_to_delete:
        cmd = f"sudo rm -f {'versions/' if loc else '/data/web_static/releases/'}{ver}"
        if loc:
            local(cmd)
        else:
            run(cmd)


def do_clean(number=0):
    """Function to delete out-of-date archives
    """
    global repeate
    number = int(number)

    if repeate is None:
        local_versions = subprocess.run(['ls', 'versions'],
                                        capture_output=True, text=True)
        repeate = 1

        if local_versions.returncode == 0:
            del_versions(local_versions.stdout, number, loc=True)

    remote_versions = run("sudo ls /data/web_static/releases")
    if remote_versions:
        del_versions(remote_versions, number, loc=None)
