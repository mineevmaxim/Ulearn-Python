import sqlite3

database = input()
table = input()

db = sqlite3.connect(database).cursor()

for row in db.execute(f'select gender, avg(height) as avg_height, sum(weight) as total_weight from {table} group by gender').fetchall():
    row = list(row)
    row[1] = round(row[1], 2)
    print(*row)