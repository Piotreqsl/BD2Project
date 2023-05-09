from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Airport, Plane, Flight, Passenger, Reservation

# Create your views here.
class AirportBaseView(View):
    model = Airport
    fields = '__all__'
    success_url = reverse_lazy('airplanes:all_airports')

class AirportListView(AirportBaseView, ListView):
    """View to list all airporsts.
    Use the 'airport_list' variable in the template
    to access all Airport objects"""

class AirportDetailView(AirportBaseView, DetailView):
    """View to show details of a single airport.
    Use the 'airport' variable in the template
    to access the Airport object."""

class AirportCreateView(AirportBaseView, CreateView):
    """View to create a new airport.
    Use the 'airport' variable in the template
    to access the Airport object."""



class AirportUpdateView(AirportBaseView, UpdateView):
    """View to update an existing airport.
    Use the 'airport' variable in the template
    to access the Airport object."""


class AirportDeleteView(AirportBaseView, DeleteView):
    """View to delete an existing airport.
    Use the 'airport' variable in the template
    to access the Airport object."""

#############################3

class PlaneBaseView(View):
    model = Plane
    fields = '__all__'
    success_url = reverse_lazy('airplanes:all_planes')

class PlaneListView(PlaneBaseView, ListView):
    """View to list all planes.
    Use the 'plane_list' variable in the template
    to access all Plane objects"""

class PlaneDetailView(PlaneBaseView, DetailView):
    """View to show details of a single plane.
    Use the 'plane' variable in the template
    to access the Plane object."""

class PlaneCreateView(PlaneBaseView, CreateView):
    """View to create a new plane.
    Use the 'plane' variable in the template
    to access the Plane object."""

class PlaneUpdateView(PlaneBaseView, UpdateView):
    """View to update an existing plane.
    Use the 'plane' variable in the template
    to access the Plane object."""

class PlaneDeleteView(PlaneBaseView, DeleteView):
    """View to delete an existing plane.
    Use the 'plane' variable in the template
    to access the Plane object."""

#############################

class FlightBaseView(View):
    model = Flight
    fields = '__all__'
    success_url = reverse_lazy('airplanes:all_flights')

class FlightListView(FlightBaseView, ListView):
    """View to list all flights.
    Use the 'flight_list' variable in the template
    to access all Flight objects"""

class FlightDetailView(FlightBaseView, DetailView):
    """View to show details of a single flight.
    Use the 'flight' variable in the template
    to access the Flight object."""

class FlightCreateView(FlightBaseView, CreateView):
    """View to create a new flight.
    Use the 'flight' variable in the template
    to access the Flight object."""

class FlightUpdateView(FlightBaseView, UpdateView):
    """View to update an existing flight.
    Use the 'flight' variable in the template
    to access the Flight object."""

class FlightDeleteView(FlightBaseView, DeleteView):
    """View to delete an existing flight.
    Use the 'flight' variable in the template
    to access the Flight object."""

#############################

class PassengerBaseView(View):
    model = Passenger
    fields = '__all__'
    success_url = reverse_lazy('airplanes:all_passengers')

class PassengerListView(PassengerBaseView, ListView):
    """View to list all passengers.
    Use the 'passenger_list' variable in the template
    to access all Passenger objects"""

class PassengerDetailView(PassengerBaseView, DetailView):
    """View to show details of a single passenger.
    Use the 'passenger' variable in the template
    to access the Passenger object."""

class PassengerCreateView(PassengerBaseView, CreateView):
    """View to create a new passenger.
    Use the 'passenger' variable in the template
    to access the Passenger object."""

class PassengerUpdateView(PassengerBaseView, UpdateView):
    """View to update an existing passenger.
    Use the 'passenger' variable in the template
    to access the Passenger object."""

class PassengerDeleteView(PassengerBaseView, DeleteView):
    """View to delete an existing passenger.
    Use the 'passenger' variable in the template
    to access the Passenger object."""

#############################

class ReservationBaseView(View):
    model = Reservation
    fields = '__all__'
    success_url = reverse_lazy('airplanes:all_reservations')

class ReservationListView(ReservationBaseView, ListView):
    """View to list all reservations.
    Use the 'reservation_list' variable in the template
    to access all Reservation objects"""

class ReservationDetailView(ReservationBaseView, DetailView):
    """View to show details of a single reservation.
    Use the 'reservation' variable in the template
    to access the Reservation object."""

class ReservationCreateView(ReservationBaseView, CreateView):
    """View to create a new reservation.
    Use the 'reservation' variable in the template
    to access the Reservation object."""

class ReservationUpdateView(ReservationBaseView, UpdateView):
    """View to update an existing reservation.
    Use the 'reservation' variable in the template
    to access the Reservation object."""

class ReservationDeleteView(ReservationBaseView, DeleteView):
    """View to delete an existing reservation.
    Use the 'reservation' variable in the template
    to access the Reservation object."""
