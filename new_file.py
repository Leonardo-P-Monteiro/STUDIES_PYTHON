import pathlib
import shutil
import zipfile



ZIPFILE_FOLDER = pathlib.Path(__file__).parent / 'ZIPFILE_FOLDER'
FILE_COMPACT = ZIPFILE_FOLDER / 'file_compact.zip'
FILE_DESCOMPACT = ZIPFILE_FOLDER / 'file_descompact.zip'
FILE_TO_COMPACT = pathlib.Path(__file__).parent / 'file_to_compact.txt'


pathlib.Path.mkdir(ZIPFILE_FOLDER, exist_ok=True)
pathlib.Path.touch(FILE_TO_COMPACT)

with open(FILE_TO_COMPACT, 'w', encoding='utf8') as file_txt:
    file_txt.write('It\'s a text for including content into the file.')
    file_txt.close()

with zipfile.ZipFile(FILE_COMPACT, 'w') as file_zip:
    file_zip.write('file_to_compact.txt')
    file_zip.close()

with zipfile.ZipFile(FILE_COMPACT, 'r') as file_list:
    file_read = file_list.namelist()
    print('This is the list of itens into the zip: \n', f'--> {file_read}')

with zipfile.ZipFile(FILE_COMPACT, 'r') as file_descompact:
    file_descompact.extractall(ZIPFILE_FOLDER)
    file_descompact.close()