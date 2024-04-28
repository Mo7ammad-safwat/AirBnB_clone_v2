#!/usr/bin/env python3
from fabric.api import *
from datetime import datetime
import os

env.user = 'ubuntu'
env.hosts = ['54.164.149.90', '18.234.107.151']
env.key_filename = '~/.ssh/id_rsa'


def do_pack():
    """ Generates a .tgz archive from the contents of the 'web_static' folder """
    try:
        if not os.path.exists("versions"):
            os.mkdir("versions")
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(now)
        local("tar -cvzf {} web_static".format(archive_path))
        return archive_path
    except:
        return None

def do_deploy(archive_path):
    """ Deploys the archive to web servers """
    if not archive_path or not os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')
        archive_file = archive_path.split("/")[-1]
        folder_name = archive_file.split(".")[0]
        release_folder = '/data/web_static/releases/' + folder_name + '/'
        run('mkdir -p ' + release_folder)
        run('tar -xzf /tmp/{} -C {}'.format(archive_file, release_folder))
        run('rm /tmp/{}'.format(archive_file))
        run('mv {}web_static/* {}'.format(release_folder, release_folder))
        run('rm -rf {}web_static'.format(release_folder))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(release_folder))
        print("New version deployed!")
        return True
    except:
        return False

def deploy():
    """ Create and deploy new archive """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
