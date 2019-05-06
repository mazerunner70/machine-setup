#!/usr/bin/env python3.6

import subprocess
import re

output = subprocess.check_output(['vboxmanage', 'list', 'extpacks']).decode('UTF-8').replace('\n',' ').split('Pack no. ')


regex = re.compile (r'Oracle VM VirtualBox Extension Pack.*(\d+\.\d+\.\d+)')

vbext_version_matches = [ regex.search(row) for row in output ]

vbext_version = [ vbext_match.group(1) for vbext_match in vbext_version_matches if vbext_match ]

if len(vbext_version)>0:
     print (vbext_version[0], end='')

