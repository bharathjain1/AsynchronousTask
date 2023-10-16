from datetime import datetime
from django.db import connection
import pytz

class db_connection:
    def __init__(self):
        self.cursor = connection.cursor()
    
    def insert(self,
                userid,
                pizza_base,
                pizza_cheese,
                pizza_toppings,
                total_price,
                order_status):
        dt_today = datetime.today()  # Local time
        current_time = dt_today.astimezone(pytz.timezone('Asia/Kolkata'))
        sql = '''INSERT INTO Orders(user_id, pizza_base,pizza_cheese,pizza_toppings,total_price,order_status,ordered_time)\
                 VALUES (%s, %s, %s, %s, %s, %s, %s)'''
        values = [userid,pizza_base,pizza_cheese,pizza_toppings,total_price,order_status,current_time]
        self.cursor.execute(sql,values)
        self.cursor.close()
    
    def read(self, orderid):
        sql = '''select * from Orders where Order_id={order_id}'''.format(order_id=orderid)
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def get_latest_orderid(self):
        sql = '''select order_id from Orders order by Order_id desc limit 1;'''
        self.cursor.execute(sql)
        return self.cursor.fetchone()
    