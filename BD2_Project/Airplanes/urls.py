from django.urls import path
from . import views


app_name = 'airports'

urlpatterns = [
    path('', views.AirportListView.as_view(), name='all'),
]