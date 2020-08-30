#!/usr/bin/python

import os

with open('version', 'r') as f:
    version = f.read()
print(f"This is version {version} of the app using config: {os.getenv('color')}!!")
print(f"$foobar = {os.getenv('foobar')}")