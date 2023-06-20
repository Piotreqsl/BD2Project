from django.urls import path
from . import views


app_name = 'airplanes'

urlpatterns = [
    path('', views.HomeView, name='home'),
    path('airport/', views.AirportListView.as_view(), name='all_airports'),
    path('airport/<int:pk>', views.AirportDetailView.as_view(), name='airport_detail'),
    path('airport/create', views.AirportCreateView.as_view(), name='airport_create'),
    path('airport/<int:pk>/update', views.AirportUpdateView.as_view(), name='airport_update'),
    path('airport/<int:pk>/delete', views.AirportDeleteView.as_view(), name='airport_delete'),
    
    path('plane/', views.PlaneListView.as_view(), name='all_planes'),
    path('plane/<int:pk>', views.PlaneDetailView.as_view(), name='plane_detail'),
    path('plane/create', views.PlaneCreateView.as_view(), name='plane_create'),
    path('plane/<int:pk>/update', views.PlaneUpdateView.as_view(), name='plane_update'),
    path('plane/<int:pk>/delete', views.PlaneDeleteView.as_view(), name='plane_delete'),

    path('flight/', views.FlightListView.as_view(), name='all_flights'),
    path('flight/<int:pk>', views.FlightDetailView.as_view(), name='flight_detail'),
    path('flight/create', views.FlightCreateView.as_view(), name='flight_create'),
    path('flight/<int:pk>/update', views.FlightUpdateView.as_view(), name='flight_update'),
    path('flight/<int:pk>/delete', views.FlightDeleteView.as_view(), name='flight_delete'),

    path("passenger/", views.PassengerListView.as_view(), name="all_passengers"),
    path("passenger/<int:pk>", views.PassengerDetailView.as_view(), name="passenger_detail"),
    path("passenger/create", views.PassengerCreateView.as_view(), name="passenger_create"),
    path("passenger/<int:pk>/update", views.PassengerUpdateView.as_view(), name="passenger_update"),
    path("passenger/<int:pk>/delete", views.PassengerDeleteView.as_view(), name="passenger_delete"),

    path("reservation/", views.ReservationListView.as_view(), name="all_reservations"),
    path("reservation/<int:pk>", views.ReservationDetailView.as_view(), name="reservation_detail"),
    path("reservation/create", views.ReservationCreateView.as_view(), name="reservation_create"),
    path("reservation/<int:pk>/update", views.ReservationUpdateView.as_view(), name="reservation_update"),
    path("reservation/<int:pk>/delete", views.ReservationDeleteView.as_view(), name="reservation_delete"),

    path("login/", views.login_user, name="login"),
    path("register/", views.register_user, name="register"),
    path("search/", views.flight_search_view, name="search"),
    path("result/", views.flight_search_results_view, name="flight_search_results"),
]