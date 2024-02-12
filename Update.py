import sqlite3

conn = sqlite3.connect('test.db')
print("Opened database successfully")

conn.execute("UPDATE EMPLOYEES1 set AGE = 67 WHERE ID=24")
conn.commit()

cursor = conn.execute("SELECT ID, NAME, AGE, SALARY FROM EMPLOYEES1")

for row in cursor:
    print("ID", row[0])
    print("NAME", row[1])
    print("AGE", row[2])
    print("SALARY", row[3])

print("Records found: ")
conn.close()