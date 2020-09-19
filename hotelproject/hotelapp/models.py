from django.db import models
import datetime

# Create your models here.
class CustomerModel(models.Model):
	custId = models.AutoField(primary_key=True)
	custName = models.CharField(max_length=50)
	custEmailId = models.CharField(max_length=50)
	custPassword = models.CharField(max_length=50)
	custContact = models.CharField(max_length=12)
	class Meta:
		db_table='customer'

	def __str__(self):
		return f'{self.custId},{self.custName},{self.custEmailId},{self.custPassword},{self.custContact}'

class RoomModel(models.Model):
	ROOM_TYPES = (
		('Standard','Standard'),
		('Deluxe','Deluxe'),
		('Luxury','Luxury')
	)

	roomId = models.AutoField(primary_key=True)
	roomType = models.CharField(max_length=30,choices=ROOM_TYPES)
	beds = models.IntegerField()
	capacity = models.IntegerField()
	date = models.DateField(("Date"), default=datetime.date.today)
	price = models.FloatField(default=0)
	status = models.CharField(max_length=50, default="-")
	def __str__(self):
		return f'{self.roomId}, {self.roomType} with {self.beds} beds for {self.capacity} people'


class BookingModel(models.Model):

	user = models.CharField(max_length=50)
	quest = models.IntegerField()
	roomId = models.IntegerField()
	roomType = models.CharField(max_length=30)
	beds = models.IntegerField()
	capacity = models.IntegerField()
	price = models.FloatField(default=0)
	check_in = models.DateField()
	check_out = models.DateField()




class AdminModel(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)