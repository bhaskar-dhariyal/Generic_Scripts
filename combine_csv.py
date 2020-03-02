import os
import glob
import pandas as pd
import click
#set working directory


@click.command()
@click.option('--path', help="Path of CSV files", required=True, type=click.Path(exists=True))
def combine(path):
    os.chdir(path)

    all_filenames = [i for i in glob.glob('*.{}'.format('csv'))]
    #print(all_filenames)

    #combine all files in the list
    combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
    #export to csv
    combined_csv.to_csv( "combined_csv.csv", index=False, encoding='utf-8-sig')
    print(f"Finished combining")

if __name__ == "__main__":
    combine()