
import sqlite3

conn = sqlite3.connect('clients.db',  check_same_thread=False)
c = conn.cursor()




class client:
    def clients_write(name,address1,address2,postcode,email,phone):
            c.execute("SELECT name FROM stuffToPlot")
            a = c.fetchall()
            for row in a:
                if row[0]==name:
                    address = address1,name
                    address102=address2,name
                    postalcode = postcode,name
                    mail = email,name
                    number = phone,name
                    c.execute('UPDATE stuffToPlot SET adress1 = ?  WHERE name = ?;',address)
                    c.execute('UPDATE stuffToPlot SET adress2 = ?  WHERE name = ?;',address102)
                    c.execute('UPDATE stuffToPlot SET postalcode = ?  WHERE name = ?;',postalcode)
                    c.execute('UPDATE stuffToPlot SET email = ?  WHERE name = ?;',mail)
                    c.execute('UPDATE stuffToPlot SET phone = ?  WHERE name = ?;',number)

                    conn.commit()
                    #c.close()
                    #conn.close()

    #clients_write("Yassa Taiseer","1328 Whitney Terrace","452 Savoline Blvd","L9E 1K5","yassataiseer@gmail.com","1234567890")
