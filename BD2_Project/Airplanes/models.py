from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

airport_name_length = 50
country_name_length = 50
person_name_length = 50
plane_name_length = 50

# class TestModel(models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()

#     def __str__(self):
#         return self.name

class Plane(models.Model):
    name = models.CharField(max_length=plane_name_length)
    def __str__(self):
        return self.name
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]

class Airport(models.Model):
    name = models.CharField(max_length=airport_name_length)
    country = models.CharField(max_length=country_name_length)
    town = models.CharField(max_length=country_name_length)
    def __str__(self):
        return self.name
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]


class Flight(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    departure_from = models.ForeignKey(Airport ,on_delete=models.CASCADE, related_name='departure_from')
    departure_at = models.DateTimeField()
    arrival_to = models.ForeignKey(Airport ,on_delete=models.CASCADE, related_name='arrival_to')
    arrival_at = models.DateTimeField()
    no_seats = models.IntegerField(default=0)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    def get_fields(self):
        return [(field.name, field.value_to_string(self))
                if field.name != 'plane' and field.name != 'departure_from' and field.name != 'arrival_to'
                else 
                (field.name, Plane.objects.get(pk=field.value_from_object(self)).name if field.name == 'plane' else Airport.objects.get(pk=field.value_from_object(self)).name)
                 for field in self._meta.fields]



class Passenger(models.Model):
    firstname = models.CharField(max_length=person_name_length)
    surname = models.CharField(max_length=person_name_length)
    age = models.IntegerField(default=18, validators=[MinValueValidator(12), MaxValueValidator(200)])
    descrption = models.TextField()
    def __str__(self):
        return self.firstname + " " + self.surname
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]

class Reservation(models.Model):
    person = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    paid = models.BooleanField()

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]

class Worker(models.Model):
    firstname = models.CharField(max_length=person_name_length)
    surname = models.CharField(max_length=person_name_length)
    age = models.IntegerField(default=18, validators=[MinValueValidator(12), MaxValueValidator(200)])
    descrption = models.TextField()
    working_on = models.ForeignKey(Airport, on_delete=models.CASCADE)
    def __str__(self):
        return self.firstname + " " + self.surname
