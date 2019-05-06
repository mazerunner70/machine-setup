#!/usr/bin/env python3.6

import subprocess
import re

output = subprocess.check_output(['apt', 'list', 'virtualbox*']).decode('UTF-8').split('\n')
regex = re.compile('virtualbox-(\d+\.\d+).*(\d+\.\d+.\d+)-')

vb_version_matches = [ regex.search(row) for row in output ]

vb_versions = [ vb_match.group(2) for vb_match in vb_version_matches if vb_match ]
print (vb_versions[-1], end='')
