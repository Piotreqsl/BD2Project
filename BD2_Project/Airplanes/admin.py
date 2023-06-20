from django.contrib import admin
from .models import Airport, Flight, Profile, Plane, Reservation, Worker

# Register your models here.
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Profile)
admin.site.register(Plane)
admin.site.register(Reservation)
admin.site.register(Worker)
