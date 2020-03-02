#**************************************************************
#*                                                            *
#*                                                            *
#* combine_csv.py                                             *
#*                                                            *
#* By: Bhaskar Dhariyal <bhaskar.dhariyal@ucdconnect.ie>      *
#*                                                            *
#* created: 03/02/20 16:16:34 by Bhaskar Dhariyal             *
#* updated: 03/02/20 17:57:06 by Bhaskar Dhariyal             *
#*                                                            *
#*                                                            *
#***********************************************************²**

import os
import glob
import pandas as pd
import click

@click.command()
@click.argument('path', required=True, type=click.Path(exists=True), nargs = 1)
@click.argument('file_name', nargs = 1)
def combine(path, file_name):
    os.chdir(path)

    all_filenames = sorted(i for i in glob.glob('*.{}'.format('csv')))

    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    combined_csv.to_csv(f"{file_name}.csv", index=False, encoding='utf-8-sig')
    print("Finished combining")

    print("Deleting temporary files")
    #for item in all_filenames:
    #    os.remove(f"{item}.csv")
        
if __name__ == "__main__":
    combine()