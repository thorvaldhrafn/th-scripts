#!/usr/bin/env bash

mkdir /usr/local/thscripts/
useradd -s /bin/bash -d /usr/local/thscripts/ -m thscripts
mkdir /usr/local/thscripts/bin && rsync -aq bin/ /usr/local/thscripts/bin/
mkdir /usr/local/thscripts/etc && rsync -aq etc/ /usr/local/thscripts/etc/
mkdir /usr/local/thscripts/web && rsync -aq web/ /usr/local/thscripts/web/
chown -R thscripts:thscripts /usr/local/thscripts/

if [[ -d /etc/nginx/ ]]
then
    cp confs/nginx_thscripts.conf /etc/nginx/conf.d/thscripts.conf
fi

cp confs/th-api.service /usr/lib/systemd/system/

cp requirements.txt /usr/local/thscripts/
su - thscripts -c "virtualenv --no-site-packages /usr/local/thscripts/.venv/ && source /usr/local/thscripts/.venv/bin/activate && pip install -r requirements.txt"
rm /usr/local/thscripts/requirements.txt

systemctl daemon-reload
systemctl enable th-api.service
systemctl restart th-api.service
