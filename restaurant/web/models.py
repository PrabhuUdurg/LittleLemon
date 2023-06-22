from django.db import models

# Create your models here.
class Booking(models.Model):
    id = models.IntegerField(max_length=11, primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(max_length=6)
    booking_date = models.DateTimeField()
    
class Menu(models.Model):
    id = models.IntegerField(max_length=5, primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(max_length=5)