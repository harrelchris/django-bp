#!/usr/bin/env bash

source /srv/web/scripts/deploy/postgres.sh

source /srv/web/scripts/deploy/app.sh

source /srv/web/scripts/deploy/gunicorn.sh

source /srv/web/scripts/deploy/nginx.sh
