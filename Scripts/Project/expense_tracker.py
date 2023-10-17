import mysql.connector
import json
from app_frontend import *

with open('Scripts\\Project\\myconfig.json','r') as c:
    params= json.load(c)['params']

print("Import success!")

mydb = mysql.connector.connect(
    host=params['host'],
    user=params['username'],
    password=params['password'],
    database= params['database'],
    port = 3306
)

mycursor = mydb.cursor()

mycursor.execute("show tables")

myresult = mycursor.fetchall()
print(myresult)


if __name__ == "__main__":
    app = ExpenseTracker()
    app.mainloop()

# Close the MySQL connection
mydb.close()
