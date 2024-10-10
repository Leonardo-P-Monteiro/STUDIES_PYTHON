# IMPORTS
import json
import shutil
import pathlib
from typing import TypedDict

# PATHS OF THE DIRECTORIES.
ABSOLUTE_PATH = pathlib.Path(__file__)
PATHLIB_FOLDER = ABSOLUTE_PATH.parent / 'PATHLIB_FOLDER'
NEW_FILE_PATH = PATHLIB_FOLDER / 'data_example_modified.json'
FILE_PATH = ABSOLUTE_PATH.parent / 'data_exemple.json'

# MAKING A DIRECTORY.
pathlib.Path.mkdir(PATHLIB_FOLDER, exist_ok=True)

# LOADING THE FILE.
if not NEW_FILE_PATH.exists():
    shutil.copy(FILE_PATH, NEW_FILE_PATH)

# CHARGING THE TYPE DICT.
class MyDictJson(TypedDict):
    id: int
    nome: str
    email: str
    telefone: str


# OPENING THE FILE AND MODIFING.
with open(NEW_FILE_PATH, '+r') as file:
    data_json = json.load(file)
    dict_data_json: MyDictJson = data_json
    dict_data_json['nome'] = 'António Guterres'
    dict_data_json['id'] = 2711
    dict_data_json['email'] = 'a.guterres@onu.org'
    dict_data_json['telefone'] = '+55 88 94755 3916'
    file.close()

# SAVING THE FILE.
with open(NEW_FILE_PATH, 'w') as file:
    json.dump(dict_data_json, file, indent=4, sort_keys= True)
    file.close()
    


