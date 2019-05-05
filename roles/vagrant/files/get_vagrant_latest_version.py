#!/usr/bin/env python3.6

import requests
import re

def hack_extract_versions(payload):
    array_versions = payload.split(r"a href")
    pattern = re.compile(r'"/vagrant/(.*)/"')
    version_matches = [ pattern.search(row) for row in array_versions ]
    versions = [ match.group(1) for match in version_matches if match]
    return versions

http_response = requests.get("https://releases.hashicorp.com/vagrant/")
payload = str(http_response.content)

print (hack_extract_versions(payload)[0], end='')
