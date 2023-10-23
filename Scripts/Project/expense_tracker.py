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

# mycursor.execute("show tables")

# myresult = mycursor.fetchall()
# print(myresult)


# if __name__ == "__main__":
#     app = ExpenseTracker()
#     app.mainloop()

usr_name="pmm"
fname = "Pranav"
lname= "M"
mob= 1234567890
dob = '2001-01-01'
gen =0
m_income = 123456789
password = "ABC!@#"


mycursor.execute(f"INSERT INTO USERSINFO(USER_NAME, FIRST_NAME, LAST_NAME, MOBILE_NUMBER, DOB, GENDER, MONTHLY_INCOME, PASSWORDS) VALUES ('{usr_name}', '{fname}', '{lname}', {mob}, '{dob}',{gen}, {m_income},'{password}')" )
                #  (usr_name,fname,lname,mob,dob,gen,m_income,password))

print("Done")

mydb.commit()

# Close the MySQL connection
mydb.close()
