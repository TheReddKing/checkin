# Setting up AWS EC2

** May be outdated **

## Additional Requirements

- nginx
- supervisor

## Steps

0. install python dependencies `pip install -r requirements.txt`
1. install postgres
1. Create Database on Server

   sudo apt-get install postgresql postgresql-contrib
   sudo su
   update-rc.d postgresql enable
   service postgresql start

1. `adduser checkin` <b> For ubuntu </b>
1. `sudo -u postgres createuser checkin`
1. `sudo -u postgres createdb <dbname>`
1. `sudo -u postgres psql`
   `alter user checkin with encrypted password '<password>';`
   `grant all privileges on database <dbname> to checkin ;`
1. Clone repo
1. Copy the `build.zip` file into the `client/` folder (or manual build it using `yarn build` in the `client/` folder)
1. Update your `config.py` file (`SQLALCHEMY_DATABASE_URI`)
1. Run `python manage.py db init`
1. Run `python manage.py db migrate`
1. Run `python manage.py db upgrade`

## Setup admin user

7. Setup your admin username password combo in `start_script.py`
8. Run `python start_script.py 0`

## Nginx

This server works best with Nginx with a service to run the server backend
Using supervisor to control service

### Install supervisor

```
sudo apt install supervisor
sudo mkdir /var/log/checkin
```

Add to `/etc/supervisord/conf.d/checkin.conf`

```
[program:checkin]
command = /home/checkin/env/bin/python run_server.py PRODUCTION
directory = /home/checkin/checkin
autostart = true
autorestart = true
user = checkin
stderr_logfile=/var/log/checkin/checkin.err.log
stdout_logfile=/var/log/checkin/checkin.out.log
```

Then run

```
sudo supervisorctl reread
sudo service supervisor restart
```

### For nginx configuration

In your site's VirtualHost (in `/etc/nginx/sites-available` ... Google how to use Nginx if you don't know how to)

```
  location /api/ {
    proxy_pass http://127.0.0.1:5000/api/;
    proxy_set_header X-Real-IP $remote_addr;
  }
  location / {
    root /home/checkin/checkin/build;
    try_files $uri $uri/ =404;
  }
```
