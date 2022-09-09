#!/usr/bin/env bash
# prepares simple nginx servers for static deployment of `web-static`
service nginx status
if (( $? != 0 )); then
    apt-get -y update
    apt-get -y install nginx
    find /var/www/html/index.html
    if (( $? != 0 )); then
        mkdir -p /var/www/html/
        echo 'Holberton School' > /var/www/html/index.html
    fi
    service nginx restart
fi

mkdir -p /data/web_static/shared/
find /data/web_static/releases/test/index.html
if (( $? != 0 )); then
    mkdir -p /data/web_static/releases/test/
    echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html
    ln -sf /data/web_static/releases/test/ /data/web_static/current
fi

chown -R ubuntu:ubuntu /data/

grep -q "location \/hbnb_static\/ {$" /etc/nginx/sites-available/default
if (( $? != 0 )); then
    cp /etc/nginx/sites-available/default /etc/nginx/sites-available/default.bup
    sed -i "0,/^\tlocation \/ {$/s/^\tlocation \/ {$/\tlocation \/hbnb_static\/ {\n\t\talias \/data\/web_static\/current\/;\n\t\tautoindex off;\n\t}\n\n\tlocation \/ {/" /etc/nginx/sites-available/default
    service nginx reload
fi
