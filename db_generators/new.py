
import sqlite3
### Do not run the code as it will create a new user code was only meant to write into a database
conn = sqlite3.connect('employees.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(firstname TEXT, lastname TEXT, email TEXT,password TEXT, dateadd TEXT, update TEXT)")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES('Mohammed','Taiseer','56Operahouse','05-Oct-2015','05-Oct-2015')")
    conn.commit()
    c.close()
    conn.close()
    
create_table()
data_entry()