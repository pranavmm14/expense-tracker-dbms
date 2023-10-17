import mysql.connector
import json

with open('config.json','r') as c:
    params= json.load(c)['params']

print("Import success!")

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="spmm"
)

print(mydb)