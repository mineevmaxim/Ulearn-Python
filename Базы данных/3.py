import sqlite3

database = input()
table = input()
mark_table = input()

db = sqlite3.connect(database).cursor()

for row in db.execute(f'select {table}.name, avg({mark_table}.mark) as avg_mark from {table} join {mark_table} on {table}.id group by {table}.id').fetchall():
    print(row[0], float(round(row[1])))