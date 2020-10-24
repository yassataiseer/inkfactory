import sqlite3

conn = sqlite3.connect('orders.db', check_same_thread=False)
c = conn.cursor()
class order_writer:##writes into orders.db
    def data_entry(ticket_number,client,employee,product,model,brand,serial_no,accessory,amount,status,description,comments,add_date,up_date):
        c.execute("INSERT INTO stuffToPlot VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(ticket_number,client,employee,product,model,brand,serial_no,accessory,amount,status,description,comments,add_date,up_date))  
        conn.commit()
    def data_fetcher():
        cursor = c.execute("SELECT * FROM stuffToPlot")
        orders = cursor.fetchall()
        return orders
    def update_data(ticket_number,client,employee,product,model,brand,serial_no,accessory,amount,status,description,comments,add_date,up_date):
        c.execute("SELECT client FROM stuffToPlot")
        a = c.fetchall()
        for row in a:
            if row[0]==client:
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
        pass

#order_writer.data_entry('00002','Yassa Taiseer','Taiseer Uddin Mohammed','Cellphone','iphone 8','apple','xxx','phone and charger','$30','pending','It is in red colour and needs new screen','give 10$ dicount','09-October-2015','09-October-2015')

print(order_writer.data_fetcher())