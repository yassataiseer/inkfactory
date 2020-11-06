import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('clients.db', check_same_thread=False)
c = conn.cursor()



class search:
    def data(name):
        send_data=[]
        c.execute('SELECT * FROM stuffToPlot')
        data = c.fetchall()
        for rows in data:
            if name==rows[0]:
                send_data.append(rows)
            else:
                pass
        return(send_data)

#print(search.data("Syed Atuer Ali"))