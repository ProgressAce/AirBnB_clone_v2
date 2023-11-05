#!/usr/bin/env bash
# Sets up my web servers for deployment of web_static folder from AirBnb_clone_2

sudo apt-get update > /dev/null
sudo apt-get install -y nginx > /dev/null
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
echo "<h2><em>I have arrived!<em><h2>" | sudo tee /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -hR ubuntu:ubuntu /data/
DIR="\n\tlocation /hbnb_static {\n \
\t\talias /data/web_static/current/;\n \
\t}"
sudo sed -i "47i\ ${DIR}" /etc/nginx/sites-available/default
sudo service nginx restart
