# Deployment

Deploy this application to a Debian virtual machine.

## Provision

Use your preferred cloud provider to create a Debian VM instance. Enable HTTP/HTTPS traffic in the firewall.

- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html
- https://cloud.google.com/compute/docs/instances/create-start-instance

## Deploy

1. Update the instance
1. Install git
1. Clone the application
1. Run deploy script
1. Create a superuser

```shell
sudo apt update
sudo apt upgrade -y
sudo apt install git -y
sudo git clone https://github.com/harrelchris/django-bp.git /srv/web
sudo bash /srv/web/scripts/deploy/deploy.sh
sudo /srv/web/.venv/bin/python3 /srv/web/app/manage.py createsuperuser
```

## Logs

```shell
# NGINX
journalctl -u nginx.service
tail /var/log/nginx/access.log
tail /var/log/nginx/error.log

# Gunicorn
journalctl -u gunicorn.socket

# Application
journalctl -u gunicorn.service

# Postgres
/var/log/postgresql/postgresql-13-main.log

# Timers
systemctl list-timers
systemctl --type=timer --all --failed

systemctl status example.timer
journalctl -u example.timer
```

## Install timer

Add to `deploy.sh`

```shell
cp /srv/web/system/example.service /etc/systemd/system/example.service
cp /srv/web/system/example.timer /etc/systemd/system/example.timer

systemctl start example.timer
systemctl enable example.timer --now
systemctl daemon-reload
```
