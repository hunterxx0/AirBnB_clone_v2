#!/usr/bin/env bash
# sets up your web servers for the deployment of web_static
sudo apt-get update -y
sudo apt-get install nginx -y
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
sudo chown -R ubuntu:ubuntu /data
echo "Hello World!" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data
sudo sed -i '37i\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx restart
