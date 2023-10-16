from django.db import models

# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Order(models.Model):
    order_id = models.AutoField(db_column='Order_id', primary_key=True)  # Field name made lowercase.
    user_id = models.IntegerField(blank=True, null=True)
    pizza_base = models.CharField(max_length=100, blank=True, null=True)
    pizza_cheese = models.CharField(max_length=100, blank=True, null=True)
    pizza_toppings = models.JSONField(blank=True, null=True)
    total_price = models.IntegerField(blank=True, null=True)
    order_status = models.CharField(max_length=100, blank=True, null=True)
    ordered_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Orders'
