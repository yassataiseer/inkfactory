import csv
import sqlite3
conn = sqlite3.connect("orders.db") # change to 'sqlite:///your_filename.db'
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(order_No TEXT, Client TEXT, Employee TEXT, product TEXT, model TEXT, brand TEXT, serial_No TEXT, Accessory TEXT, Amount TEXT, Status TEXT, Description TEXT, Comments TEXT, add_data TEXT, Up_date TEXT)")
#code base is meant to setup the basics for the orders.db file
c.close()
conn.close()
    

