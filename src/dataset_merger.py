# NOTE: Run this script to merge both dataset files...
import os
import pandas as pd

def merge_csv_files(file1_path, file2_path, output_path):
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    # Concat based on headers.
    df2.columns = df1.columns
    merged_df = pd.concat([df1, df2], ignore_index=True)
    merged_df.to_csv(output_path, index=False)

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
