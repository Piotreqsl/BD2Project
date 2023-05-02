from django.views import View
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Airport, Plane, Flight

# Create your views here.
class AirportBaseView(View):
    model = Airport
    fields = '__all__'
    success_url = reverse_lazy('airports:all')

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