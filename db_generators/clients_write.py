import sqlite3
### Do not run the code as it will create a new user code was only meant to write into a database
conn = sqlite3.connect('clients.db', check_same_thread=False)
c = conn.cursor()
class writer:
    def data_entry(name,address1,address2,postalcode,email,phone):
        c.execute("INSERT INTO stuffToPlot VALUES(?,?,?,?,?,?)",(name,address1,address2,postalcode,email,phone))
        conn.commit()

#writer.data_entry("Tester Last","1234 fake st","432 real st", "L5N 1S0","help@gmail.com","1234567890")
    