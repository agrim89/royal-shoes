# DoctorBox-Server

A web application that provides a RESTful API for DoctorBox mobile clients as well as a web-based admin tool to
update the content exposed to the mobile clients.  

Written in python3 using [Django](https://www.djangoproject.com/) and [django-rest-framework](http://www.django-rest-framework.org/).   

## Installation

### Install `python3` and `virtualenv`
```
brew install python3
pip3 install virtualenv
brew install postgresql
```

## Common tasks

### Run the server locally
`./local.sh`

### Run tests and ensure compliance with [PEP8](https://www.python.org/dev/peps/pep-0008/)
```
./test.sh
```

### Create a local superuser to log into the admin backend
```
source env/bin/activate
./manage.sh createsuperuser
```

### Log into the admin backend
Visit `http://localhost:8000/admin/` in your local web browser.

### Browse the RESTful API
Visit `http://localhost:8000/api/1/` in your local web browser.
