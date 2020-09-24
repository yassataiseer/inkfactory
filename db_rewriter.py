
import sqlite3

conn = sqlite3.connect('employees.db')
c = conn.cursor()


class table_edit:

    def write(firstname,lastname,email,password,newdate):
        c.execute("SELECT Email FROM stuffToPlot")
        a = c.fetchall()
        for row in a:
            print (row[0])
            if row[0]==email:
                print("90% DONE")
                data = firstname,email
                c.execute('UPDATE stuffToPlot SET firstname = ?   WHERE Email = ?;',data)
                print("100% DONE")
                conn.commit()
                c.close()
                conn.close()


            #c.execute("INSERT INTO stuffToPlot VALUES('firstname','lastname','Email','password','newdate') values(?,?,?,?,?",(self,firstname,lastname,email,password,newdate(firstname,lastname,email,password,newdate)

#           
# return True
#        else:
#            pas
    


print(table_edit.write("Taiseerrrr","Mohammeddddd","taiseer142@hotmail.com","123abc","20-09-2020"))


