import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('employees.db', check_same_thread=False)
c = conn.cursor()



class gather:
    def data(email):
        send_data=[]
        
        c.execute('SELECT * FROM stuffToPlot')
        data = c.fetchall()
        for rows in data:
            if email==rows[2]:
                send_data.append(rows)
            else:
                pass
        return(send_data)

#print(gather.data("--"))