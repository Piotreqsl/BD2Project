from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

airport_name_length = 50
country_name_length = 50
person_name_length = 50
plane_name_length = 50


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
    departure_from = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='departure_from')
    departure_at = models.DateTimeField()
    arrival_to = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_to')
    arrival_at = models.DateTimeField()
    no_seats = models.IntegerField(default=0)
    plane = models.ForeignKey(Plane, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_fields(self):
        list = [(field.name, field.value_to_string(self))
                if field.name != 'plane' and field.name != 'departure_from' and field.name != 'arrival_to'
                else
                (field.name, Plane.objects.get(
                    pk=field.value_from_object(self)).name if field.name == 'plane' else Airport.objects.get(
                    pk=field.value_from_object(self)).name)
                for field in self._meta.fields]

        reservation_count = Reservation.objects.filter(flight=self.id, paid=True).count()
        list.append(('reservation_count', reservation_count))
        free_places = self.no_seats - reservation_count
        list.append(('free_places', free_places))
        return list


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    age = models.IntegerField(default=18, validators=[MinValueValidator(12), MaxValueValidator(200)])
    description = models.TextField()

    def __str__(self):
        return str(self.user)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in self._meta.fields]

@receiver(post_save, sender=User)
def create_user_passenger_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_user_passenger_profile(sender, instance, created, **kwargs):
    instance.profile.save()

class Reservation(models.Model):
    person = models.ForeignKey(Profile, on_delete=models.CASCADE)
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
