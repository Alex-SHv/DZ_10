import sqlite3

connection = sqlite3.connect("test_DB.sl3", 5)
cur = connection.cursor()
cur.execute("INSERT INTO first_table (name) VALUES ('Boris');")
cur.execute("INSERT INTO first_table (name) VALUES ('Ivan');")
cur.execute("INSERT INTO first_table (name) VALUES ('Michael');")
cur.execute("INSERT INTO first_table (name) VALUES ('Dmitriy');")
cur.execute("INSERT INTO first_table (name) VALUES ('Konrad');")
cur.execute("INSERT INTO first_table (name) VALUES ('Vitaliy');")
connection.commit()
cur.execute("SELECT rowid, name FROM first_table;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()