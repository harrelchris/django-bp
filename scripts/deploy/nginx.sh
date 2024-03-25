#!/usr/bin/env bash

apt install nginx -y

cp /srv/web/app.conf /etc/nginx/conf.d/app.conf

PUBLIC_IP=$(curl -s -4 ifconfig.me)
sed -i "s/server_name ~^.+$;/server_name $PUBLIC_IP;/" /etc/nginx/conf.d/app.conf

systemctl daemon-reload
systemctl restart nginx
