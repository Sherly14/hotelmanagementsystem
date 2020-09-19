from django.contrib import admin
from .models import CustomerModel,RoomModel,BookingModel,AdminModel

# Register your models here.
admin.site.register(CustomerModel)
admin.site.register(RoomModel)
admin.site.register(BookingModel)
admin.site.register(AdminModel)

