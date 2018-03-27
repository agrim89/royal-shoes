#!/usr/bin/env bash

source ./setup.sh

function run_locally {

    python manage.py migrate
    gunicorn royalshoes.wsgi -b 0.0.0.0:$PORT --access-logfile - --error-logfile - --log-level debug
}

eval_in_virtual_environment run_locally
