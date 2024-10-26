from pathlib import Path
import sqlite3

DIR_FOLDER = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = DIR_FOLDER / DB_NAME
TABLE_NAME = 'Customes'

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#SQLite tasks

# Creating the table.
cursor.execute(
    f'CREATE TABLE IF NOT EXISTS {TABLE_NAME}'
    '('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
    ')'
)
connection.commit()

# Clearling all table.

cursor.execute(
    f'DELETE FROM {TABLE_NAME}'
)

# Clearling the table sqlite_sequence

cursor.execute(
    f'DELETE FROM sqlite_sequence WHERE name="{TABLE_NAME}"'
)


# Values to register on table columns.
values_insert = (
                ('Alvaro Monteiro', 68.9),
                ('Lívia Damasceno', 56.7), 
                ('Isabela Martins', 56.8),
                ('João Pedro', 43.8),
                ('Lucas Laurentino', 80.4)
                )

comand_insert = f'INSERT INTO {TABLE_NAME} (name, weight) VALUES (?, ?)'

# cursor.execute(
#     f'INSERT INTO {TABLE_NAME}'
#     '(id, name, weight)'
#     'VALUES'
#     '(NULL, "Albetiza Braga", 54),'
#     '(NULL, "Antônio Mauriço", 76.8),'
#     '(NULL, "Luiz Cláudio", 65.7)'
# )
cursor.executemany(comand_insert, values_insert)

connection.commit()


# Updating informations of table.

cursor.execute(
    f'UPDATE {TABLE_NAME} SET name = "Edgar Barbosa" WHERE id = "1"'
)

# Deleting datas

cursor.execute(
    f'DELETE FROM {TABLE_NAME} WHERE id = "5"'
)

connection.commit()

#SQLite connection closure.
cursor.close()
connection.close()


if __name__ == '__main__':
    print('ok')