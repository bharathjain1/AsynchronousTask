from django.urls import path

from . import views

urlpatterns = [
    path("placeOrder/", views.placeOrder),
    path("Orderdetails/", views.Orderdetails)
]