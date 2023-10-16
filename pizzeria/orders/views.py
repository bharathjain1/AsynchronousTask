from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from orders.task import update_order_status
from . connections import db_connection
import json

# Create your views here.

# This view is used to create orders and execute them fully until delivered
@api_view(['POST'])
def placeOrder(request):
    data = request.data
    if len(data) <= 0:
        return Response({"ERror":"Please add data properly"})
    for i in range(len(data)):
        userid = data[i]['userid']
        pizza_base = data[i]['pizza_base']
        pizza_cheese = data[i]['pizza_cheese']
        pizza_toppings = json.dumps([item.strip(" '") for item in data[i]['pizza_toppings'].strip("{}").split(',')])
        total_price = 500 #Any pizza same price [We can change the rates using dictionary and add the sum as well]
        order_status = "placed"
        db_connection().insert(userid,pizza_base,pizza_cheese,pizza_toppings,total_price,order_status)
        order_id = db_connection().get_latest_orderid()[0]
        update_order_status.delay(order_id)
    return Response(data)


# This view is used to give users the summary/track details about the orders
@api_view()
def Orderdetails(request):
    order_id = request.GET.get('order_id')
    if order_id is None:
        return Response({'Please Enter the order id'})
    data = db_connection().read(order_id)
    if data is None:
        return Response("Order you have asked for does not exist")
    order_details = {
        "user_id" : data[1],
        "pizza_toppings" : json.loads(data[4]),
        "order_status" : data[6]
    }
    return Response(order_details)