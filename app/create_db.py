# THIS FILE WILL CREATE THE DATABASE users

import mysql.connector
mydb = mysql.connector.connect(
host = 
user = 
passwd = 
)

my_cursor = mydb.cursor()
my_cursor.execute('CREATE DATABASE IF NOT EXISTS hackathon_2')
