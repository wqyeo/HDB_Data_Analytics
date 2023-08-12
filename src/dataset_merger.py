# NOTE: Run this script to merge both dataset files...
import os
import pandas as pd

def merge_csv_files(file1, file2, output_file):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Reorder the columns of the second DataFrame to match the first
    df2 = df2[df1.columns]
    merged_df = pd.concat([df1, df2], ignore_index=True)

    # Remove dupes
    merged_df.drop_duplicates(inplace=True)
    merged_df.to_csv(output_file, index=False)

# NOTE: Set file locations. Output file will be in the same path as well...
file_locations = os.path.join("src", "datasets")

# NOTE: Set file names, only support `.csv` formats for now.
file1_name = "HDB Dataset - Jan.csv"
file2_name = "HDB Dataset - Feb.csv"
output_name = "HDB_merged_output.csv"

file1_path = os.path.join(file_locations, file1_name)
file2_path = os.path.join(file_locations, file2_name)
output_path = os.path.join(file_locations, output_name)

merge_csv_files(file1_path, file2_path, output_path)
print("CSV files merged successfully.")
