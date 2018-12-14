import sqlite3
from employee import Employee

conn = sqlite3.connect("employee.db")

c = conn.cursor()

first_name=input("Enter first name ")
last_name=input("Enter Last Name ")

emp_1 = Employee(first_name,last_name)


c.execute("INSERT INTO Employee values(?, ?)",(emp_1.first,emp_1.last))
'''c.execute("""CREATE TABLE Employee (
         first_name text,
         last_name text)""")
c.execute("INSERT INTO Employee values('change','new ')")'''

c.execute("""Select * from Employee""")
print(c.fetchall())

conn.commit()
conn.close()