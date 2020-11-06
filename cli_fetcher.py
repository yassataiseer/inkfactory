import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('clients.db', check_same_thread=False)
c = conn.cursor()



class sheets:
    def data():
        send_data=[]
        c.execute('SELECT * FROM stuffToPlot')
        data = c.fetchall()
        #print(data)
        send_data = []
        for rows in data:
            send_data.append(rows)
        return( send_data)
    def name_data():#gets name of person
        send_data=[]
        c.execute('SELECT name FROM stuffToPlot')
        data = c.fetchall()
        #print(data)
        send_data = []
        for rows in data:
            send_data.append(rows)
        return( send_data)

#a = sheets.data()
#print(a[0])
#print(sheets.name_data())

#a = sheets.name_data()
#for i in a :
#    print (i[0])