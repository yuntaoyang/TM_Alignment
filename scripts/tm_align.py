#!/usr/bin/env python
# coding: utf-8

"""
Run TM-Align for two PDB files.
"""

import os
import re
import argparse
import shutil
import subprocess

def get_parser():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description='Run TM-Align for two PDB files.')
    parser.add_argument('--pdb_dir_1', required=True, help='The directory of the first PDB file')
    parser.add_argument('--pdb_dir_2', required=True, help='The directory of the second PDB file')
    parser.add_argument('--out_dir', required=True, help='The directory of the output file')
    return parser

def build_script(pdb_dir_1, pdb_dir_2):
    command = ["./scripts/TMalign_cpp", pdb_dir_1, pdb_dir_2, '-o', 'TM_sup']
    return command

def format_output(out_dir):
    # Copy and rename TM_sup_all_atm to the output directory
    shutil.copy2('TM_sup_all_atm', os.path.join(out_dir))
    # Remove all the output
    for file in os.listdir('./'):
        if file[0:3] == 'TM_':
            os.remove(file)
        else:
            continue

def get_tm_score(out_dir):
    with open(out_dir, 'r') as file:
        lines = file.readlines()
    target_line = lines[16]
    tm_score = re.search(r'TM-score=([\d.]+)', target_line).group(1)
    return tm_score

def main():
    parser = get_parser()
    args = parser.parse_args()
    try:
        # Run TM-align
        command = build_script(args.pdb_dir_1, args.pdb_dir_2)
        process = subprocess.run(command, capture_output=True, text=True)
        # Format the output
        format_output(args.out_dir)
        # Get TM-score from the PDB file
        tm_score = get_tm_score(args.out_dir)
        print(tm_score)
    except:
        print(process.stdout)

if __name__ == "__main__":
    main()
