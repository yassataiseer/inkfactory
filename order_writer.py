'''
This is the order's class halfway through the project I realized it is easier to put all db related task in one big class
data_entry puts writes data into orders.db
data_fetcher gets data from orders.db to pass into html tables
update_data updates data allowing changes to be made
'''

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
    def ticket_builder():
        cursor = c.execute("SELECT order_No FROM stuffToPlot")
        number = cursor.fetchall()
        number = number[0]
        for x in number :
            return int(x)+1
        
    def not_done_orders():
        package = []
        cursor = c.execute("SELECT * FROM stuffToPlot")
        orders = cursor.fetchall()
        for i in orders:
            package.append(i[9])
        return package
        
    def update_data(ticket_number,client,employee,product,model,brand,serial_no,accessory,amount,status,description,comments,add_date,up_date):
        c.execute("SELECT client FROM stuffToPlot")
        a = c.fetchall()
        for row in a:
            if row[0]==client:
                ticket_data = ticket_number,client
                employee_data = employee, client
                product_data = product,client
                model_data = model, client
                brand_data = brand, client
                serial_no = serial_no, client
                accessory_data = accessory, client
                amount_data = amount,client 
                status_data = status,client
                description_data = description,client
                comments_data = comments,client
                add_date_data = add_date, client
                up_date_data = up_date, client
                c.execute('UPDATE stuffToPlot SET order_No = ?  WHERE client = ?;',ticket_data)
                c.execute('UPDATE stuffToPlot SET Employee = ?  WHERE client = ?;',employee_data)
                c.execute('UPDATE stuffToPlot SET product = ?  WHERE client = ?;',product_data)
                c.execute('UPDATE stuffToPlot SET model = ?  WHERE client = ?;',model_data)
                c.execute('UPDATE stuffToPlot SET brand = ?  WHERE client = ?;',brand_data)
                c.execute('UPDATE stuffToPlot SET serial_no = ?  WHERE client = ?;',serial_no)
                c.execute('UPDATE stuffToPlot SET Accessory = ?  WHERE client = ?;',accessory_data)
                c.execute('UPDATE stuffToPlot SET Amount = ?  WHERE client = ?;',amount_data)
                c.execute('UPDATE stuffToPlot SET Status = ?  WHERE client = ?;',status_data)
                c.execute('UPDATE stuffToPlot SET Description = ?  WHERE client = ?;',description_data)
                c.execute('UPDATE stuffToPlot SET Comments = ?  WHERE client = ?;',comments_data)
                c.execute('UPDATE stuffToPlot SET add_data = ?  WHERE client = ?;',add_date_data)
                c.execute('UPDATE stuffToPlot SET Up_date = ?  WHERE client = ?;',up_date_data)
                
                conn.commit()

#order_writer.update_data('00004','Yassa Taiseer','Taiseer Uddin Mohammed','Cellphone','iphone 69','apple','xxx','phone and charger','$30','pending','It is in red colour and needs new screen','give 10$ dicount','09-October-2015','09-October-2015')

#print(order_writer.data_fetcher())
#print(order_writer.ticket_builder())

a = order_writer.not_done_orders()
print(a)