import sqlite3

database = input()
table = input()

db = sqlite3.connect(database)

for row in db.execute(f'select id, name from {table} where gender = "male" and height > 1.8 order by name'):
    print(str(row[0]), str(row[1]), sep=' ', end='\n')