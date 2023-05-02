from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

airport_name_length = 50
country_name_length = 50
person_name_length = 50
plane_name_length = 50

class TestModel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name

class Plane(models.Model):
    name = models.CharField(max_length=plane_name_length)
    def __str__(self):
        return self.name

class Flight(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    departure_from = models.CharField(max_length=airport_name_length)
    departure_at = models.TimeField()
    arrival_to = models.CharField(max_length=airport_name_length)
    arrival_at = models.TimeField()
    no_seats = models.IntegerField(default=0)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class Airport(models.Model):
    name = models.CharField(max_length=airport_name_length)
    country = models.CharField(max_length=country_name_length)
    town = models.CharField(max_length=country_name_length)
    def __str__(self):
        return self.name
    
    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]

class Passenger(models.Model):
    firstname = models.CharField(max_length=person_name_length)
    surname = models.CharField(max_length=person_name_length)
    age = models.IntegerField(default=18, validators=[MinValueValidator(12), MaxValueValidator(200)])
    descrption = models.TextField()
    def __str__(self):
        return self.firstname + " " + self.surname

class Reservation(models.Model):
    person = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    paid = models.BooleanField()

class Worker(models.Model):
    firstname = models.CharField(max_length=person_name_length)
    surname = models.CharField(max_length=person_name_length)
    age = models.IntegerField(default=18, validators=[MinValueValidator(12), MaxValueValidator(200)])
    descrption = models.TextField()
    working_on = models.ForeignKey(Airport, on_delete=models.CASCADE)
    def __str__(self):
        return self.firstname + " " + self.surname
