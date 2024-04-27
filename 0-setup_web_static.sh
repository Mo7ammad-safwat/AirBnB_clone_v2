#!/usr/bin/env bash
# Script that sets up your web servers for the deployment of web_static.

SITE_FILE=/etc/nginx/sites-available/default
END_POINT='\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}\n'
HTML_CONTENT=\
"<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>"

CHECK_HBNB=$(grep 'location /hbnb_static' < "$SITE_FILE")

sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y install nginx
sudo mkdir -p '/data/web_static/releases/test/'
sudo mkdir -p '/data/web_static/shared/'
sudo touch '/data/web_static/releases/test/index.html'
sudo ln -sf /data/web_static/releases/test /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
echo "$HTML_CONTENT" > '/data/web_static/releases/test/index.html'

if [ -z "$CHECK_HBNB" ]; then
	sudo sed -i "s@^\tserver_name _;@&$END_POINT@" $SITE_FILE
fi

sudo service nginx restart
