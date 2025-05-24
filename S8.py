import pandas as pd
import sqlite3 as sql

data = pd.read_csv('/Users/grygoriiboiko/Desktop/DATA/Employees.csv')

conn = sql.connect('employees.db')
data.to_sql('employees', conn, if_exists='replace')
cursor = conn.cursor()
cursor.execute("SELECT * FROM employees")
print(cursor.fetchall())

conn.close()
