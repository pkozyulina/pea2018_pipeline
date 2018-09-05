#!/usr/bin/env python3

import os
import glob
import argparse
import re
from collections import defaultdict
import pandas as pd

parser = argparse.ArgumentParser(description='Script creates a summary from all the files of *.isoforms.results of RSEM output in the directory')
parser.add_argument("-dir", help="Input directory path to read all files from", default=False)
parser.add_argument("-out", help="Output file name", default='RSEMsummary.csv')
parser.add_argument("-counts", help="Chose if you need raw extimated counts (raw) or TPM (tpm). Default is TPM", default='tpm')
parser.add_argument("-pat", help="Chose if you need per gene (gene) or per isoform (isoform) counts. Default is 'per isiform'", default='isoform')
args = parser.parse_args()


## summary type (per gene or per isoform)
if args.pat == 'gene':
    pattern = '*.gene.results'
else:
    pattern = '*.isoforms.results'


## counts type
if args.counts == 'raw':
    counts = 4
else:
    counts = 5



current_dir = None
if args.dir:
    current_dir = args.dir
else:
    current_dir = os.getcwd()



allSamples = defaultdict()
for filename in glob.glob(os.path.join(current_dir, pattern)):

    samplename = re.split(r'\.', re.split(r'/', filename)[-1])[0]
    sample = defaultdict()
    with open(filename, 'r') as file:
        next(file)
        for line in file:
            temp = re.split('\t', line.strip())
            sample[temp[0]] = temp[counts]
            #print(temp[0], temp[counts])

    allSamples[samplename] = sample

dfSamples = pd.DataFrame(allSamples)
print(dfSamples)

dfSamples.to_csv(args.out)