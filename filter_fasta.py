#!/usr/bin/env python3

from Bio import SeqIO
import argparse
from collections import defaultdict
import re

# Parsing fastq
def parse_fasta(input_file):
    for record in SeqIO.parse(input_file, "fasta"):
        yield str(record.seq), record.id



def main():
    # parsing command line arguments
    parser = argparse.ArgumentParser(description='Filter fasta file based on a list of sequence IDs')
    parser.add_argument('-inp', '--input', help='Input fastq file', required=True)
    parser.add_argument('-id', '--fastaid', help='Input file with list of fasta IDs', required=True, metavar='File', type=argparse.FileType(),)
    parser.add_argument('-out', '--output', help='Output name of a filtered file', required=True)
    args = parser.parse_args()
    print(args)
    ################# CREATE A LIST OF READS NEEDED ######################################
    id_list = set()
    for line in args.fastaid:
        print(line.strip())
        id_list.add(line.strip())

    SeqIO.write([record for record in SeqIO.parse(args.input, "fasta") if record.id in id_list], args.output, "fasta")




if __name__ == '__main__':
    main()