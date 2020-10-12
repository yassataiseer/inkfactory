import csv
import sqlite3
conn = sqlite3.connect("orders.db", check_same_thread=False) # change to 'sqlite:///your_filename.db'
c = conn.cursor()
a = '00003','Yassa Taiseer','Taiseer Uddin Mohammed','Cellphone','iphone 8','apple','xxx','phone and charger','$30','pending','It is in red colour and needs new screen','give 10$ dicount','09-October-2015','09-October-2015'
c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(order_No TEXT, Client TEXT, Employee TEXT, product TEXT, model TEXT, brand TEXT, serial_No TEXT, Accessory TEXT, Amount TEXT, Status TEXT, Description TEXT, Comments TEXT, add_data TEXT, Up_date TEXT)")
#code base is meant to setup the basics for the orders.db file
#c.execute("INSERT INTO stuffToPlot VALUES('00001','Yassa Taiseer','Taiseer Uddin Mohammed','Cellphone','iphone 8','apple','xxx','phone and charger','$30','pending','It is in red colour and needs new screen','give 10$ dicount','09-October-2015','09-October-2015')")
#c.execute("INSERT INTO stuffToPlot VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",a)
conn.commit()
c.close()
conn.close()
    

