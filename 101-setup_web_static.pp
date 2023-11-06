# Puppet setup for preparing servers based on script/task 0

package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
}

file { '/data':
  ensure => 'directory'
}

file { '/data/web_static':
  ensure => 'directory'
}

file { '/data/web_static/releases':
  ensure => 'directory'
}

file { '/data/web_static/releases/test':
  ensure => 'directory'
}

file { '/data/web_static/shared':
  ensure => 'directory'
}

file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => '<b>Yes! I have arrived!</b>\n'
}

file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test/'
}

exec { 'change /data/ ownership':
  command => 'chown -hR ubuntu:ubuntu /data/',
  path    => '/usr/bin/:/usr/local/bin/:/bin/'
}

$nginx_conf = "server {
	listen 80 default_server;
	listen [::]:80 default_server;
	root /var/www/html;
	add_header X-Served-By ${hostname};
	index index.html index.htm index.nginx-debian.html;

	server_name _;
 
	location /hbnb_static/ {
 		alias /data/web_static/current/;
		index index.html index.htm;
 	}

	location / {
		try_files $uri $uri/ =404;
	}"

file { '/var/www':
  ensure => 'directory'
}

file { '/var/www/html':
  ensure => 'directory'
}

file { '/var/www/html/index.html':
  ensure  => 'present',
  content => 'The index.\n'
}

#file { '/var/www/html/404.html'
#  ensure  => 'present',
#  content => ''FILL IN
#}

file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf
}

exec { 'restart nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
