import os
import pandas as pd
import csv


# Read in usable_subs.txt and generate a list of sub-##### to be used for file filtering
def read_usable_subs(filename):
    with open(filename, 'r') as file:
        usable_subs = [line.strip() for line in file]
    return usable_subs


# Eliminate any sub-##### that aren't specified in usable_subs.txt
def eliminate_subs(filename, usable_subs):
    with open(filename, 'r') as file:
        lines = file.readlines()

    header = lines[0]  
    data_lines = lines[1:]  

    filtered_data_lines = [line for line in data_lines if any(line.strip().startswith(id) for id in usable_subs)]

    with open(filename, 'w') as file:
        file.write(header)  
        file.writelines(filtered_data_lines)


# Format the first column for BIDS specification
# This function applies "participant_id to the first cell for every measure and applies sub- to the beginning of every ID"
def format_first_column(filename):
    with open(filename, 'r') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    if rows:
        for row in rows[1:]:
            if row and len(row) > 0:
                row[0] = f'sub-{row[0]}'

    with open(filename, 'w', newline='') as infile:
        writer = csv.writer(infile)
        writer.writerows(rows)

    with open(filename, 'r') as infile:
                lines = infile.readlines()

    if lines:
        header = lines[0]
        header = header.replace(header.split('\t')[0], "participant_id")

    with open(filename, 'w') as infile:
        infile.write(header)
        infile.writelines(lines[1:])
    

# Iterate through the .tsv that were generated to elimante unwanted subs and apply BIDS formatting
def process_files(folder_path, usable_subs):
    for filename in os.listdir(folder_path):
        if filename.endswith('.tsv'):
            file_path = os.path.join(folder_path, filename)

            with open(file_path, 'r') as infile:
                reader = csv.reader(infile)
                rows = list(reader)

            with open(file_path, 'w', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerows(rows)

            eliminate_subs(file_path, usable_subs)
            format_first_column(file_path)

            print(f"Processed: {file_path}")


# File converts all .txt files that exist in /rawdata for processing defined above
# Todo: figure out why the script breaks if I put this about the process_files function 
def convert_to_tsv(input_path, output_path):
    for filename in os.listdir(input_path):
        if filename.endswith('.txt'):
            txt_file_path = os.path.join(input_path, filename)
            tsv_file_path = os.path.join(output_path, filename.replace('.txt', '.tsv'))

            df = pd.read_csv(txt_file_path, sep='\t', na_values=["n/a"])
            df.to_csv(tsv_file_path, sep='\t', index=False, na_rep="n/a")

            print(f"Converted: {txt_file_path} to {tsv_file_path}")


# Specify paths and call functions
if __name__ == "__main__":
    usable_subs = read_usable_subs('/Users/coopersharp/Desktop/usable_subs.txt')
    input_path = '/Users/coopersharp/Desktop/rawdata'  # Specify the folder path containing the .txt files
    output_path = '/Users/coopersharp/Desktop/data_paper' # .tsv output will be generated here

    convert_to_tsv(input_path, output_path)
    process_files(output_path, usable_subs)
