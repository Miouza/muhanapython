import sqlite3
conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("INSERT INTO EMPLOYEES1 (ID,NAME,AGE,SALARY) values (21, 'Musa', 23, 230000)")
conn.execute("INSERT INTO EMPLOYEES1 (ID,NAME,AGE,SALARY) values (22, 'Milna', 24, 240000)")
conn.execute("INSERT INTO EMPLOYEES1 (ID,NAME,AGE,SALARY) values (23, 'Moha', 27, 2430000)")
conn.execute("INSERT INTO EMPLOYEES1 (ID,NAME,AGE,SALARY) values (24, 'Masha', 28, 43000)")


conn.commit()
print("Records inserted successfully")
conn.close()