from django.db import models

# Create your models here.
class car_detail(models.Model):
	car_number			= models.CharField(max_length=20)
	diesel_fuel			= models.BooleanField(default='True')
	

