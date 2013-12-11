# coding: utf-8
import os

import boto
from fabric.api import *

LOCAL_DIR = os.path.dirname(__file__)
boto_config_file = os.path.join(LOCAL_DIR, 'deploy', 'boto.cfg')
if not os.path.exists(boto_config_file):
    abort("Please create deploy/boto.cfg file with AWS credentials")
boto.config.load_from_path(boto_config_file)

# we need to import this one after boto.config.load_from_path
from fabix.aws import ec2


PROJECT_DIR = '/var/www/libra/'


@task
def prod():
    """Configure env variables for production"""
    env.user = 'ubuntu'
    env.hosts = ['ec2-107-21-234-26.compute-1.amazonaws.com']


@task
def setup():
    """Setup project"""
    packages = 'nginx python python-pip gcc python2.7-dev'

    with prefix('DEBIAN_FRONTEND=noninteractive'):
        sudo('apt-get update')
        sudo('apt-get -y install {}'.format(packages))

    sudo('mkdir -p {}'.format(PROJECT_DIR))
    sudo('mkdir -p /var/log/libra')

    sudo('pip install virtualenv')
    sudo('virtualenv {}virtualenv'.format(PROJECT_DIR))

    install_requirements()
    put(os.path.join(LOCAL_DIR, 'deploy', 'upstart.conf'),
        '/etc/init/libra.conf', use_sudo=True)
    put(os.path.join(LOCAL_DIR, 'deploy', 'nginx-site.conf'),
        '/etc/nginx/sites-enabled/libra.conf', use_sudo=True)
    sudo('rm -f /etc/nginx/sites-enabled/default')
    execute(nginx, 'restart')


def install_requirements():
    requirements = os.path.join(LOCAL_DIR, 'requirements.txt')
    python_packages = open(requirements).read().replace('\n', ' ')
    sudo('{}virtualenv/bin/pip install {}'.format(PROJECT_DIR, python_packages))


@task
def setup_autoscale():
    """Setup AWS autoscale"""
    my_id = 'wedding_plattform'

    kwargs = {
        "ami_id": 'ami-3fec7956',  # Official Ubuntu 12.04.1 LTS US-EAST-1
        "instance_type": "t1.micro",
        "key_name": my_id,
        "security_groups": [my_id],
        "availability_zones": ["us-east-1a", "us-east-1b", "us-east-1d"],
        "min_instances": 0,
        "sp_up_adjustment": 1,
        "load_balancers": [my_id]
    }
    ec2.setup_autoscale(my_id, **kwargs)


@task
def update_autoscale(instance_id):
    """Update autoscale configuration"""
    ec2.update_autoscale(instance_id, 'wedding_plattform')


@task
def deploy():
    """Deploy project to server"""
    local("find . -name '*.pyc' -print0|xargs -0 rm -rf", capture=False)
    local("find . -name '.sass-cache' -print0|xargs -0 rm -rf", capture=False)

    install_requirements()

    sudo('rm -rf {}libra'.format(PROJECT_DIR))
    put(os.path.join(LOCAL_DIR, 'libra'), PROJECT_DIR, use_sudo=True)

    # move settings
    with cd("{}libra/".format(PROJECT_DIR)):
        sudo('mv settings_prod.py settings.py')

    execute(restart)


@task
def start():
    """Start application service"""
    sudo('start libra')


@task
def stop():
    """Stop application service"""
    sudo('stop libra')


@task
def restart():
    """Stop and start application service"""
    with settings(warn_only=True):
        execute(stop)
    execute(start)


@task
def nginx(op):
    """Manage nginx service"""
    sudo('service nginx {}'.format(op))
