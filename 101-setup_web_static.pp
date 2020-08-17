#!/usr/bin/env bash
# configure web-02 to be identical to web-01.
exec {'setup':
command  => 'apt-get update -y; apt-get install nginx -y; mkdir -p /data/web_static/shared/ /data/web_static/releases/test/; touch /data/web_static/releases/test/index.html; chown -R ubuntu:ubuntu /data; echo "Hello World!" > /data/web_static/releases/test/index.html; ln -sf /data/web_static/releases/test/ /data/web_static/current; chown -R ubuntu:ubuntu /data; sed -i '37i\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default; sudo service nginx restart;
',
provider => shell,
}
