import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('employees.db', check_same_thread=False)
c = conn.cursor()



class employee_finder:
    def generate_data():#generates data from employees.db
        send_data=[]
        c.execute('SELECT * FROM stuffToPlot')
        data = c.fetchall()
        #print(data)
        send_data = []
        for rows in data:
            send_data.append(rows)
        return( send_data)
    def update_data(firstname,lastname,email,password,newdate):#update data in employees.db
        c.execute("SELECT Email FROM stuffToPlot")
        a = c.fetchall()
        for row in a:
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

    def data(email):#fetches data from the email column
        send_data=[]
        c.execute('SELECT * FROM stuffToPlot')
        data = c.fetchall()
        for rows in data:
            if email==rows[2]:
                send_data.append(rows)
            else:
                pass
        return(send_data)
        
    def query(users):
        send_data=[]
        c.execute('SELECT * FROM stuffToPlot')
        data = c.fetchall()
        #print(data)
        for rows in data:
            print(rows[2])
            print(rows[3])
            if users[0]==rows[2] and users[1]==rows[3]:
                return True

            else:
                pass
        return( send_data)


            


#print(static.data())