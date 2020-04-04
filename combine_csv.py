
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
    temp_path = '..'
    combined_csv.to_csv(os.path.join(temp_path + f"/{file_name}.csv"), index=False, encoding='utf-8-sig')
    print("Finished combining")

    print("Deleting temporary files")
    for item in all_filenames:
        os.remove(item)
        
if __name__ == "__main__":
    combine()
