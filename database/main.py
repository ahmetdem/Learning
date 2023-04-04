import mysql.connector
  
# Connecting from the server
mydb = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = "a123654_Y",
    database = "testdb")
 
mycursor = mydb.cursor()

sqlformula = 'INSERT INTO visitors (name, age) VALUES (%s, %s)'
visitors = [('Ahmet', 19),
           ('Can', 18),
           ('Melisa', 22),
           ('Dilara', 35),
           ('Mert', 10)]

mycursor.executemany(sqlformula, visitors)

mydb.commit()

