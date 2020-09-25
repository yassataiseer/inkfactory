
import sqlite3

conn = sqlite3.connect('employees.db',  check_same_thread=False)
c = conn.cursor()


class table_edit:

    def write(firstname,lastname,email,password,newdate):
        c.execute("SELECT Email FROM stuffToPlot")
        a = c.fetchall()
        for row in a:
            print (row[0])
            if row[0]==email:
                fname = firstname,email
                lname = lastname,email
                password_edit=password,email
                date_changer = newdate,email
                c.execute('UPDATE stuffToPlot SET firstname = ?  WHERE Email = ?;',fname)
                c.execute('UPDATE stuffToPlot SET lastname = ?  WHERE Email = ?;',lname)
                c.execute('UPDATE stuffToPlot SET password = ?  WHERE Email = ?;',password_edit)
                c.execute('UPDATE stuffToPlot SET newdate = ?  WHERE Email = ?;',date_changer)
                conn.commit()
                #c.close()
                #conn.close()



#print(table_edit.write("Taiseer","Mohammed","taiseer142@hotmail.com","56Operahouse","20-09-2020"))


