from django.contrib import admin
from .models import Airport, Flight, Passenger, Plane, Reservation, Worker
# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)
admin.site.register(Plane)
admin.site.register(Reservation)
admin.site.register(Worker)