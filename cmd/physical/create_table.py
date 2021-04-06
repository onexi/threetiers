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

# create database
cursor = cnx.cursor()
query = ('''
USE movies;
CREATE TABLE music(
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100),
    release_year YEAR(4),
    genre VARCHAR(100),
    collection_in_mil INT
)
''')
cursor.execute(query)
cnx.commit()
cursor.close()
cnx.close()