
  
import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('employees.db', check_same_thread=False)
c = conn.cursor()




class data_answer:
    def data(users):
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

            
'''

email = "adil@theinkfactory.ca"
password = "1234567890"
variable = email,password
#print(list(variable))
print(data_answer.data(variable))
'''