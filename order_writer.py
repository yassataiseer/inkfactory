import sqlite3

conn = sqlite3.connect('order.db', check_same_thread=False)
c = conn.cursor()
class order_writer:##writes into orders.dn
    def data_entry(ticket_number,client,employee,product,model,brand,serial_no,accessory,status,description,comments,date):
        c.execute("INSERT INTO stuffToPlot VALUES(?,?,?,?,?,?,?,?,?,?,?)",(ticket_number,client,employee,product,model,brand,serial_no,accessory,status,description,comments,date))
        conn.commit()


order_writer.data_entry('00001','Huawei	Mate 2','front screen replaced','Cellphone','xxxxxxxxxxxxxxxxxx','09-October-2015')