from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import CreateLoginForm, RegisterUserForm
from .models import Airport, Plane, Flight, Profile, Reservation


# Create your views here.

def HomeView(request):
    return render(request, 'home.html')
def login_user(request):
    if request.method == "POST":
        form = CreateLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            # obsługa logowania
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('airplanes:flight')

            # nie udało się
            info = "The logging in was unsuccessful"
            return render(request, 'login.html', {"form": form, "info": info})
    else:
        form = CreateLoginForm()
        return render(request, 'login.html', {"form": form})

def logout_user(request):
    logout(request)
    return redirect('airplanes:home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]

            # obsługa rejestracji
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('airplanes:login')

            # nie udało się
            info = "The registration was unsuccessful"
            return render(request, 'register.html', {"form": form, "info": info})
        else:
            info = "The password is not strong enough"
            return render(request, 'register.html', {"form": form, "info": info})
    else:
        form = RegisterUserForm()
        return render(request, 'register.html', {"form": form})


def flight_search_view(request):
    airports = Airport.objects.all()
    if request.method == "POST":
        return redirect('airplanes:flight_search_results')
    else:
        return render(request, 'flight_search.html', {"airports": airports})


def flight_search_results_view(request):
    arrival = request.GET["arrival"]
    departure = request.GET['departure']
    arrival_airport = Airport.objects.get(name=arrival)
    departure_airport = Airport.objects.get(name=departure)
    ##reuslt with get fields method


    results = Flight.objects.filter(arrival_to=arrival_airport.id, departure_from=departure_airport.id)

    
    return render(request, 'flight_search_results.html', {"flights": results})

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
    model = Profile
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
