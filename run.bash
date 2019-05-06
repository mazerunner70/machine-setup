#!/bin/bash

ansible-playbook -i "localhost" --ask-become-pass --connection=local site.yml

