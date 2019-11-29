# Installation
**For Centos7**

yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm

yum -y install python python-pip python-virtualenv git rsync

git clone https://github.com/thorvaldhrafn/th-scripts.git

cd th-scripts

bash install.sh

**For Debian/Ubuntu**

apt update && apt -y install python python-pip python-virtualenv git rsync

git clone https://github.com/thorvaldhrafn/th-scripts.git

cd th-scripts

bash install.sh

**For Ansible**

If you use Ansible, you can install scripts with playbook th-scripts-install.yml