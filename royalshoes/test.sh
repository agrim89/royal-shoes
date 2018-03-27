#!/usr/bin/env bash

source ./setup.sh

function ensure_pep_8_and_test {
    APPLICATION_NAME=royalshoes
    flake8 ${APPLICATION_NAME} --exclude royal-shoes/royalshoes/migrations --ignore E501
    FLAKE_STATUS=$?

    python manage.py test
    TEST_STATUS=$?

    if [[ ( ${FLAKE_STATUS} == 0 ) && ( ${TEST_STATUS} == 0 ) ]] ; then
        echo "Congratulations! ${APPLICATION_NAME} is PEP8 compliant and all tests pass."
        exit 0
    else
        exit 1
    fi
}

eval_in_virtual_environment ensure_pep_8_and_test
