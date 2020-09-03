import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('employees.db', check_same_thread=False)
c = conn.cursor()



class static:
    def data():
        send_data=[]
        c.execute('SELECT * FROM stuffToPlot')
        data = c.fetchall()
        #print(data)
        send_data = []
        for rows in data:
            send_data.append(rows)
        return( send_data)

#print(static.data())