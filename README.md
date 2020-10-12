# ckanext-extrafields

## Introduction

This is a plugin for CKAN, to add extra fields relevant to the kinds of data we will add to the data catalogue. 
It is written using the documentation [here](https://docs.ckan.org/en/2.9/extensions/tutorial.html) and 
[here](https://docs.ckan.org/en/2.9/extensions/adding-custom-fields.html). It has been implemented into a new CKAN 2.9.0 installation
from source.

## Installation

* Having got the basic CKAN working, glone this repo in `/usr/lib/ckan/default/src` - so that the `ckanext-extrafields` sits in that folder, alongside `ckan` and `ckanext-ldap`.
* Activate the virtual environment with `. /usr/lib/ckan/default/bin/activate`
* `pip install -r https://raw.githubusercontent.com/ckan/ckan/ckan-2.9.0/dev-requirements.txt`
* `cd ckanext-extrafields` and `python setup.py develop`
* `nano /etc/ckan/default/ckan.ini` and add `extrafields` onto the `ckan.pkugins` line.
* `sudo service supervisor restart` and hopefully all will be well. Otherwise check `/etc/ckan/default/uwsgi.ERR` for logs.

