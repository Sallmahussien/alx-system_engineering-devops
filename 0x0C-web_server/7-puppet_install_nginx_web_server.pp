#Configuring your server with Puppet

exec { 'apt update':
  command => 'sudo apt-get update',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
}

package { 'nginx':
  ensure => installed,
}

exec { 'Nginx HTTP':
  command => 'sudo ufw allow "Nginx HTTP"',
  path    => '/usr/sbin:/usr/bin:/sbin:/bin',
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

file { '/usr/share/nginx/html/custom_404.html':
  content => 'listen 80 default_server;\n\terror_page 404',
}

file { '/etc/nginx/sites-enabled/default':
  content =>
  'server {
    listen 80 default_server;
    error_page 404 /custom_404.html;
    location = /custom_404.html {
      root /usr/share/nginx/html;
      internal;
    }
    listen [::]:80 default_server;


    root /var/www/html;

    # Add index.php to the list if you are using PHP
    index index.html index.htm index.nginx-debian.html;

    server_name _;
    rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
  

    location / {
      # First attempt to serve request as file, then
      # as directory, then fall back to displaying a 404.
      try_files $uri $uri/ =404;
    }
  }',
}	
