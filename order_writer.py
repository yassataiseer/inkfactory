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
        number = number[-1]
        for x in number :
            return int(x)+1
        
    def not_done_orders():
        package = []
        cursor = c.execute("SELECT * FROM stuffToPlot")
        orders = cursor.fetchall()
        for i in orders:
            if i[9]=="Completed":
                pass
            else:
                package.append(i)
        return package
    def order_finder(order_No):
        send_data=[]
        c.execute('SELECT * FROM stuffToPlot')
        data = c.fetchall()
        for rows in data:
            if order_No==rows[0]:
                send_data.append(rows)
            else:
                pass
        return(send_data)
    def update_data(ticket_number,client,employee,product,model,brand,serial_no,accessory,amount,status,description,comments,add_date,up_date):
        c.execute("SELECT order_No FROM stuffToPlot")
        a = c.fetchall()
        for row in a:
            
            if row[0]==ticket_number:
                clien_data = client,ticket_number
                employee_data = employee, ticket_number
                product_data = product,ticket_number
                model_data = model, ticket_number
                brand_data = brand, ticket_number
                serial_no_data = serial_no, ticket_number
                accessory_data = accessory, ticket_number
                amount_data = amount,ticket_number 
                status_data = status,ticket_number
                description_data = description,ticket_number
                comments_data = comments,ticket_number
                up_date_data = up_date, ticket_number
                #c.execute('UPDATE stuffToPlot SET order_No = ?  WHERE client = ?;',ticket_data)
                c.execute('UPDATE stuffToPlot SET client = ?  WHERE order_No = ?;',clien_data)
                c.execute('UPDATE stuffToPlot SET Employee = ?  WHERE order_No = ?;',employee_data)
                c.execute('UPDATE stuffToPlot SET product = ?  WHERE order_No = ?;',product_data)
                c.execute('UPDATE stuffToPlot SET model = ?  WHERE order_No = ?;',model_data)
                c.execute('UPDATE stuffToPlot SET brand = ?  WHERE order_No = ?;',brand_data)
                c.execute('UPDATE stuffToPlot SET serial_no = ?  WHERE order_No = ?;',serial_no_data)
                c.execute('UPDATE stuffToPlot SET Accessory = ?  WHERE order_No = ?;',accessory_data)
                c.execute('UPDATE stuffToPlot SET Amount = ?  WHERE order_No = ?;',amount_data)
                c.execute('UPDATE stuffToPlot SET Status = ?  WHERE order_No = ?;',status_data)
                c.execute('UPDATE stuffToPlot SET Description = ?  WHERE order_No = ?;',description_data)
                c.execute('UPDATE stuffToPlot SET Comments = ?  WHERE order_No = ?;',comments_data)
                c.execute('UPDATE stuffToPlot SET Up_date = ?  WHERE order_No = ?;',up_date_data)
                
                conn.commit()

#order_writer.update_data('1','Yassa Taiseer','Taiseer Uddin Mohammed','Cellphone','iphone 69','apple','xxx','phone and charger','$30','pending','It is in red colour and needs new screen','give 10$ dicount','09-October-2015','09-October-2015')

#print(order_writer.data_fetcher())
#print(order_writer.ticket_builder())

#a = order_writer.not_done_orders()
#print(a)


#a = order_writer.order_finder('5')
#print(a)