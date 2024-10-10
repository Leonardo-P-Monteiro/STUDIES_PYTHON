# IMPORTS
import pathlib
import csv
import shutil

# DIRECTORIES PATHS
CSV_FOLDER = pathlib.Path(__file__).parent / 'CSV_FOLDER'
FILE_CSV = pathlib.Path(__file__).parent / 'file_test_csv.csv'
NEW_FILE_CSV = CSV_FOLDER / 'file_test_csv_2.csv'

# MAKING THE FOLDER
pathlib.Path.mkdir(CSV_FOLDER, exist_ok= True)

# CREATING THE FILE.
NEW_FILE_CSV.touch()

# CHARGING THE FILE
dict_inf_csv = []
with open(FILE_CSV, 'r', encoding='utf8') as file_csv_r:
# READING THE INFO
    dict_reader_csv = csv.DictReader(file_csv_r)

    for information in dict_reader_csv:
        print(information, '\n')
        dict_inf_csv.append(information)


# COPYING THE INFO TO OTHER FILE

dict_csv_new_info= {
    'Name':'Isaac Correia do Amaral',
    'Age': 75,
    'Weight': '68,2',
    'Height': '1.65'
}

with open(NEW_FILE_CSV, 'w', encoding= 'utf8', newline='') as file_csv_w:
    head_file_csv = dict(dict_inf_csv[1]).keys()
    writter_csv = csv.DictWriter(file_csv_w, fieldnames=head_file_csv)
    writter_csv.writeheader()
    writter_csv.writerows(dict_inf_csv)
    writter_csv.writerow(dict_csv_new_info)

