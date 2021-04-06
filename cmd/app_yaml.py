# pip install pyyaml
import yaml
import mysql.connector

#  not safe - python will complain
# db = yaml.load(open('db.yaml'))

db = yaml.safe_load(open('db.yaml'))
config = {
    'user':     db['user'], 
    'password': db['pwrd'],
    'host':     db['host'],
    'database': db['db'],
    'auth_plugin': 'mysql_native_password'
}
cnx = mysql.connector.connect(**config)

cursor = cnx.cursor()
query = ("SELECT * FROM colleges")
cursor.execute(query)

# print all the first cell of all the rows
for row in cursor.fetchall():
    print(row)

cursor.close()
cnx.close()