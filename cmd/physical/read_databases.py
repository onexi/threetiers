import yaml
import mysql.connector

db = yaml.safe_load(open('../db.yaml'))
config = {
    'user':     db['user'], 
    'password': db['pwrd'],
    'host':     db['host'],
    'database': db['db'],
    'auth_plugin': 'mysql_native_password'
}
cnx = mysql.connector.connect(**config)

# get list of databases
cursor = cnx.cursor()
query = ("SHOW DATABASES")
cursor.execute(query)

# show list of databases
for row in cursor.fetchall():
    print(row)

cursor.close()
cnx.close()