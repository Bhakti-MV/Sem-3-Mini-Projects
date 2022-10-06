import sqlite3
 
from sqlite3 import Error
 
def sql_connection():
   try:
     conn = sqlite3.connect('mydatabase.db')
     return conn
   except Error:
     print(Error)
 
def sql_table(conn):
   cursorObj = conn.cursor()
# Create the table
   cursorObj.execute("CREATE TABLE student(student_id n(5), name char(30), city char(35), pointer decimal(7,2));")
# Insert records
   cursorObj.executescript("""
   INSERT INTO student VALUES(5001,'James Hoog', 'New York', 0.15);
   INSERT INTO student VALUES(5002,'Nail Knite', 'Paris', 0.25);
   INSERT INTO student VALUES(5003,'Pit Alex', 'London', 0.15);
   INSERT INTO student VALUES(5004,'Mc Lyon', 'Paris', 0.35);
   INSERT INTO student VALUES(5005,'Paul Adam', 'Rome', 0.45);
   """)
   
   conn.commit()

   cursorObj.execute("SELECT * FROM student")
   rows = cursorObj.fetchall()
   print("Student details:")
   for row in rows:
       print(row)
       
sqllite_conn = sql_connection()
sql_table(sqllite_conn)
if (sqllite_conn):
 sqllite_conn.close()
 print("\nThe SQLite connection is closed.")
