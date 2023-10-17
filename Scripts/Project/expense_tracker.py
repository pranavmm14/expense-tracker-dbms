import mysql.connector
import json

with open('Scripts\Project\myconfig.json','r') as c:
    params= json.load(c)['params']

print("Import success!")

mydb = mysql.connector.connect(
  host="localhost",
  user=params['username'],
  password=params['password'],
  database= params['database']
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM ")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)