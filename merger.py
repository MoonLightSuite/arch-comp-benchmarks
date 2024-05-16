import pandas as pd
import glob

# Get a list of all CSV files in the output directory and its subdirectories
csv_files = glob.glob('output/**/*.csv', recursive=True)

# Initialize an empty list to hold dataframes
dfs: list[pd.DataFrame] = []

# Loop through the list of CSV files
for csv_file in csv_files:
    # Read each CSV file into a DataFrame and append it to the list
    print(f'Reading {csv_file}')
    dfs.append(pd.read_csv(csv_file, sep=',', quotechar='"',  # type: ignore
               skipinitialspace=True))

# Concatenate all dataframes in the list
merged_df = pd.concat(dfs, ignore_index=True)  # type: ignore

# Write the concatenated dataframe to a new CSV file
merged_df.to_csv('output/merged.csv', index=False)
