#!/usr/bin/env bash
# Install Nginx and configure it

apt-get -y update
apt-get install -y nginx 
mkdir -p /data/
mkdir -p /data/web-static/
mkdir -p /data/web-static/releases/test/
mkdir -p /data/web-static/shared/
mkdir -p /data/web-static/current/
echo "<!DOCTYPE html>
<html>
        <head>
                <title>Holberton School</title>
        </head>
        <body>
                <h1>Holberton School</h1>
        </body>
</html>" > /data/web_static/releases/test/index.html
ln -sf /data/web-static/releases/test /data/web-static/current
chown -R ubuntu:ubuntu /data
sed -i "/server_name _;/a location /hbnb_static {\\n\\talias /data/web_static/current/;\\n\\t}\\n" /etc/nginx/sites-available/default
service nginx restart