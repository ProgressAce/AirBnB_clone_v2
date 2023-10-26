#!/usr/bin/env bash
# Sets up my web servers for deployment of web_static. It should:
# 
# Installs Nginx if it not already installed
# Creates the folder /data/ if it doesn’t already exist
# Creates the folder /data/web_static/ if it doesn’t already exist
# Creates the folder /data/web_static/releases/ if it doesn’t already exist
# Creates the folder /data/web_static/shared/ if it doesn’t already exist
# Creates the folder /data/web_static/releases/test/ if it doesn’t already exist
# Creates a fake HTML file /data/web_static/releases/test/index.html (with simple content, to test your Nginx configuration)
# Creates a symbolic link /data/web_static/current linked to the /data/web_static/releases/test/ folder.
#     If the symbolic link already exists, it deletes and recreats every time the script is run.
# Gives ownership of the /data/ folder to the <ubuntu> user AND group (you can assume this user and group exist).
#     This should be recursive; everything inside is then created/owned by this <ubuntu> user/group.
# Updates the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static (ex: https://mydomainname.tech/hbnb_static).
#     Nginx is restarted after updating the configuration

sudo apt-get update
sudo apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
chown -R ubuntu:ubuntu /data/

echo "<h2><em>I have arrived!<em><h2>" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current

DIR="\tlocation /hbnb_static {\n \
\t\talias /data/web_static/current/;\n \
\t}\n"
sed "54i%${DIR}" /etc/nginx/sites-available/default

sudo service nginx restart
