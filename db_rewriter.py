
import sqlite3

conn = sqlite3.connect('employees.db')
c = conn.cursor()


class table_edit:

    def write(firstname,lastname,email,password,newdate):
        c.execute("SELECT Email FROM stuffToPlot")
    for row in c.fetchall():
        #print (row[0])         #  <-- is always guaranteed to be the color value
        if row[0]=="email":
            c.execute("INSERT INTO stuffToPlot VALUES('firstname','lastname','Email','password','newdate') values(?,?,?,?,?",(self,firstname,lastname,email,password,newdate(firstname,lastname,email,password,newdate)
#            return True
#        else:
#            pass
    
#    conn.commit()
#    c.close()
#    conn.close()


print(table_edit.write("Taiseer","Mohammed","Taiseer142@hotmail.com","123abc","20-09-2020"))


