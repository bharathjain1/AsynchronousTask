# tasks.py
from celery import shared_task
from datetime import datetime, timedelta,timezone
from . models import Order
import time
import pytz
import time

#This is an async function which will run in background.
@shared_task
def update_order_status(orderid):
    time.sleep(60)
    order = Order.objects.get(order_id=orderid)
    current_time = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
    timestamp = datetime.strptime(str(order.ordered_time), '%Y-%m-%d %H:%M:%S%z')
    ordered_time = datetime.strptime(timestamp.strftime('%Y-%m-%d %H:%M:%S'), '%Y-%m-%d %H:%M:%S')
    if order.order_status == 'placed' and int((current_time-ordered_time).seconds) >= 60:
        order.order_status = 'Preparing'
        order.save()
    time.sleep(120)
    current_time = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
    if order.order_status == 'Preparing' and int((current_time-ordered_time).seconds) >= 180:
        order.order_status = 'Dispatched'
        order.save()
        time.sleep(2)
    time.sleep(120)
    current_time = datetime.strptime(datetime.now().strftime('%Y-%m-%d %H:%M:%S'),'%Y-%m-%d %H:%M:%S')
    if order.order_status == 'Dispatched' and int((current_time-ordered_time).seconds) >= 300:
        order.order_status = 'Delivered'
        order.save()
