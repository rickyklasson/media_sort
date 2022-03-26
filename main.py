#! /usr/bin/python3
import argparse
import os
import shutil

from os import path

"""
Takes a folder on unsorted images and videos and sorts them into
a YEAR -> MONTH folder structure. The filenames are expected to be
on the format: [IMG|VID]_YYYYMMDD_HHMMSS.* .
"""

def main(args):
    # 1. Get all files that are to be sorted.
    input_files = os.listdir(args.input)

    print(f'Initiating sort of folder: {args.input}. Sorted folder: {args.output}')
    # 2. For each file... get its year and month. Put in in year -> month path inside sorted folder.
    for idx, filename in enumerate(input_files):
        print(f"Copying file: {idx+1}/{len(input_files)}", end="\r")

        # Get date from filename. Format: YYYYMMDD
        datestr = filename.split('_')[1]
        year = datestr[0:4]
        month = datestr[5:6].zfill(2)

        output_folder = path.join(args.output, year, month)
        try:
            os.makedirs(output_folder)
        except FileExistsError as err:
            # Don't do anything if folder already exists.
            pass
            
        src_path = path.join(args.input, filename)
        dest_path = path.join(output_folder, filename)
        shutil.copy(src_path, dest_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Takes unsorted media files in one folder and sorts them into another folder.")
    
    parser.add_argument("-i", "--input", type=str, required=True, help="Input folder of unsorted media files.")
    parser.add_argument("-o", "--output", type=str, required=True, help="Output folder of sorted media files. \
        This folder is created if it does not exist.")

    args = parser.parse_args()
    main(args)