#!/usr/bin/env python3

import os
import glob
import re


current_dir = os.getcwd()
pattern = r'*.bam'

DATASETNAME = False
DIRPATH = False

### SETTING CONSTANTS ###

filepaths = glob.glob(os.path.join(current_dir, pattern))

with open('rsem.json', 'w') as outp:
    outp.write('{\n    \"samples\": {\n')

    for filepath in filepaths:

        filename = re.split(r'\.', re.split(r'/', filepath)[-1])[0]
        outp.write('        \"%s\": \"%s\",\n' % (filename, filepath))

        if not DATASETNAME:
            DATASETNAME = re.split(r'_', filename)[0]

        if not DIRPATH:
            DIRPATH = '/'.join(re.split(r'/', filepath)[0:-1])

    outp.write('    }}')