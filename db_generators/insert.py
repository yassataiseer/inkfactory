
import sqlite3

conn = sqlite3.connect('employees.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot( firstname TEXT, lastname TEXT, Email TEXT, password TEXT, add_date TEXT, newdate TEXT)")

def data_entry():
    c.execute("INSERT INTO stuffToPlot VALUES('Mohammed','Taiseer','taiseer142@hotmail.com','56Operahouse','05-Oct-2015','05-Oct-2015')")
    c.execute("INSERT INTO stuffToPlot VALUES('Adil','Fisk','adil@theinkfactory.ca','1234567890','16-Jan-2017','16-Jan-2017')")
    c.execute("INSERT INTO stuffToPlot VALUES('Rafael','Almida','rafael@theinkfactory.ca','1234567890','16-Jan-2017','16-Jan-2017')")
    c.execute("INSERT INTO stuffToPlot VALUES('Repair','Depo','service@theinkfactory.ca','abc123','13-Oct-2017','13-Oct-2017')")

    conn.commit()
    c.close()
    conn.close()
    
create_table()
data_entry()
