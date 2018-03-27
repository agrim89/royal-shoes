#!/usr/bin/env bash

source ./setup.sh

function push {
    cf set-env royalshoes 'ALLOWED_HOSTS' "royalshoes.cfapps.io"
    cf push royalshoes -b python_buildpack
}

eval_in_virtual_environment push
