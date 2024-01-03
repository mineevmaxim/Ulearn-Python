import pandas as pd
import sqlite3


database_name = input()
csv_file = input()
table_name = input()

df = pd.read_csv(csv_file)
db = sqlite3.connect(database_name)
df.to_sql(table_name, db)

