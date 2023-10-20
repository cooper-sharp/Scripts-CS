import os
import pandas as pd
import csv

def read_target_numbers(filename):
    with open(filename, 'r') as file:
        target_numbers = [line.strip() for line in file]
    return target_numbers

def filter_rows(filename, target_numbers):
    with open(filename, 'r') as file:
        lines = file.readlines()

    header = lines[0]  # Save the header
    data_lines = lines[1:]  # Exclude the header from processing

    filtered_data_lines = [line for line in data_lines if any(line.strip().startswith(target) for target in target_numbers)]

    with open(filename, 'w') as file:
        file.write(header)  # Rewrite the header
        file.writelines(filtered_data_lines)

def format_first_row(filename):
    with open(filename, 'r') as infile:
        reader = csv.reader(infile)
        rows = list(reader)

    if rows:
        for row in rows[1:]:
            if row and len(row) > 0:
                # Add "sub-" prefix to the first column
                row[0] = f'sub-{row[0]}'
    

    with open(filename, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerows(rows)

def process_files(folder_path, target_numbers):
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)

            # Replace "ID" with "participant_id" in the first row of each file
            with open(file_path, 'r') as infile:
                reader = csv.reader(infile)
                rows = list(reader)

            if rows and "ID" in rows[0]:
                rows[0] = [cell.replace("ID", "participant_id") for cell in rows[0]]

            with open(file_path, 'w', newline='') as outfile:
                writer = csv.writer(outfile)
                writer.writerows(rows)

            filter_rows(file_path, target_numbers)

            # Add "sub-" prefix to the first column
            format_first_row(file_path)

            print(f"Processed: {file_path}")

def convert_to_tsv(input_path, output_path):
    for filename in os.listdir(input_path):
        if filename.endswith('.txt'):
            txt_file_path = os.path.join(input_path, filename)
            tsv_file_path = os.path.join(output_path, filename.replace('.txt', '.tsv'))

            df = pd.read_csv(txt_file_path, sep='\t', na_values=["n/a"])  # Read the processed .txt file with "N/A" values
            df.to_csv(tsv_file_path, sep='\t', index=False, na_rep="n/a")  # Convert and save as .tsv with "N/A" values

            print(f"Converted: {txt_file_path} to {tsv_file_path}")

if __name__ == "__main__":
    target_numbers = read_target_numbers('/Users/coopersharp/Desktop/usable_subs.txt')
    input_path = '/Users/coopersharp/Desktop/rawdata'  # Specify the folder path containing the .txt files
    output_path = '/Users/coopersharp/Desktop/data_paper'

    process_files(input_path, target_numbers)
    convert_to_tsv(input_path, output_path)

