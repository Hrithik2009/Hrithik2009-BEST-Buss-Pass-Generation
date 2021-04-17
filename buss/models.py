from django.db import models

# Create your models here.


class Passenger(models.Model):
	CATEGORY = (
		('Monthly', 'Monthly'),
		('quarderly', 'quarderly'),
		('Yearly', 'Yearly'),
		)
	id = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=200, null=True)
	last_name = models.CharField(max_length=200, null=True)
	source = models.CharField(max_length=200, null=True)
	dest = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	date_created = models.DateTimeField(auto_now_add=200, null=True)

	def __str__(self):
		return self.first_name

class Place(models.Model):
	src = models.CharField(max_length=200, null=True)
	dest = models.CharField(max_length=200, null=True)
	fare = models.CharField(max_length=200, null=True)