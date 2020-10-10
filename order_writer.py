import sqlite3

conn = sqlite3.connect('order1.db', check_same_thread=False)
c = conn.cursor()
class order_writer:##writes into orders.dn
    def data_entry(ticket_number,client,employee,product,model,brand,serial_no,accessory,amount,status,description,comments,add_date,up_date):
        c.execute("INSERT INTO stuffToPlot VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(ticket_number,client,employee,product,model,brand,serial_no,accessory,amount,status,description,comments,add_date,up_date))
        
        conn.commit()


order_writer.data_entry('00001','Yassa Taiseer','Taiseer Uddin Mohammed','Cellphone','iphone 8','apple','xxx','phone and charger','$30','pending','It is in red colour and needs new screen','give 10$ dicount','09-October-2015','09-October-2015')