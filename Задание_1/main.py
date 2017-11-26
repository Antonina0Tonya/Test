import sqlite3
conn = sqlite3.connect('Base.sqlite3')

cursor = conn.cursor()
cursor.execute("CREATE TABLE first(name text, age integer, comment text)")
data = [ ('Anna', '21', 'www'),('Victor', '21', 'www'),('Vasia', '31', 'www')]
cursor.executemany("INSERT INTO first VALUES (?,?,?)", data)
conn.commit()

cursor.execute("CREATE TABLE second(name text, age integer, comment text)")
data = [ ('Anna', '44', 'wtw'),('Olga', '26', 'oow'),('Vasia', '31', 'www')]
cursor.executemany("INSERT INTO second VALUES (?,?,?)", data)
conn.commit()

print("First table")
cursor.execute("SELECT * FROM first")
print(cursor.fetchall()) 
print("Second table")
cursor.execute("SELECT * FROM second")
print(cursor.fetchall())
#INSERT INTO second 
cursor.execute("INSERT INTO second SELECT first.name,first.age,first.comment FROM  first LEFT JOIN second ON first.name=second.name AND first.age=second.age AND first.comment=second.comment WHERE second.age is NULL AND second.name is NULL AND second.comment is NULL")

print("Result in second table")
cursor.execute("SELECT * FROM second")
print(cursor.fetchall())
conn.close()