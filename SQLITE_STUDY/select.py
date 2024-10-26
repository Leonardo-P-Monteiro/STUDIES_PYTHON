import sqlite3
from main import TABLE_NAME, DB_FILE

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()


cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)


for row in cursor.fetchall():
    _id, name, weight = row

    print(_id, name, weight)


cursor.execute(
    f'SELECT * FROM {TABLE_NAME}'
)

cursor.arraysize = 2

print()
for row in cursor.fetchmany():
    print(row)

print()

print(cursor.fetchone())
