import dotenv
import pymysql
import os

dotenv.load_dotenv()

connect = pymysql.connect(
    host = os.environ['MYSQL_HOST'],
    user = os.environ['MYSQL_USER'],
    password = os.environ['MYSQL_PASSWORD'],
    database = os.environ['MYSQL_DATABASE']
)

print('Connection Successful\n')


cursor = connect.cursor()

#Insertion declaration SQL done through positional values.
# sql_command =(
#                 'INSERT INTO '
#                 'users '
#                 '(first_name, last_name, email, password_hash) '
#                 'VALUES '
#                 '(%s, %s, %s, %s)'
#                 )

#Insertion declaration SQL done through dictionary values.
sql_command =(
                'INSERT INTO '
                'users '
                '(first_name, last_name, email, password_hash) '
                'VALUES '
                '(%(first_name)s, %(last_name)s, %(email)s, %(password_hash)s)'
                )

#Data in format of tuple.
# data_insert = ('Jaesley', 'Monteiro', 'j@email.com', '1234afdf')
data_insert = {
                 'first_name':'Jaesley',
                 'last_name':'Monteiro', 
                 'email':'fagdj@email.com', 
                 'password_hash':'12dfdffdsf34afdf'
    }

cursor.execute(sql_command, data_insert)
cursor.execute('SELECT * FROM users')

for i in cursor.fetchall():
    if i[1] == 'Jaesley':
        for j in i:
            print(j)

connect.commit()

cursor.close()
connect.close()