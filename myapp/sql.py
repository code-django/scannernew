import sqlite3
connection=sqlite3.connect("myapp_data_to.db")
cursor=connection.cursor()
sql="""
CREATE TABLE MYAPP_DATATable(
symbol TEXT,
data1 TEXT)
"""
cursor.execute(sql)
print("database has been created")
connection.commit()
connection.close