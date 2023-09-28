# Configuring your server with Puppet

exec { 'apt update':
  command => 'sudo apt-get update',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
}

package { 'nginx':
  ensure => installed,
  notify => Service['nginx'],
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

exec { 'Nginx HTTP':
  command => 'sudo ufw allow "Nginx HTTP"',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}

file { '/etc/nginx/sites-enabled/default':
  ensure  => file,
  content => 'server {
    listen 80 default_server;
    server_name _;

    location / {
      root   /var/www/html;
      index  index.html index.htm index.nginx-debian.html;
      try_files $uri $uri/ =404;
    }

    location = /redirect_me {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
  }',
  require => Package['nginx'],
  notify  => Service['nginx'],
}	
