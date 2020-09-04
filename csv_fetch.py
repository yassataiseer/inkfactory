import csv
import sqlite3
conn = sqlite3.connect("clients.db") # change to 'sqlite:///your_filename.db'
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS stuffToPlot(name TEXT, adress1 TEXT, adress2 TEXT,postalcode TEXT, email TEXT, phone TEXT)")

#code base is meant to only take data from csv and pass into db file nothing more do not run!!
with open('tur_cli.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        #print(row)
        conn.execute("INSERT INTO stuffToPlot VALUES(?,?,?,?,?,?);",(row[0],row[1],row[2],row[3],row[4],row[5]))
        conn.commit()
c.close()
conn.close()
    

