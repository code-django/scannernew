import sqlite3
connection=sqlite3.connect("db.db")
cursor=connection.cursor()

with open('myproject/event.csv','r') as file:
    records=0
    for row in file:
        cursor.execute("INSERT INTO myapp_data Table VALUES(?,?)", row.split(","))
        connection.commit()
        records+=1
connection.close()
print('\n{} records transfer completed'.format(records))