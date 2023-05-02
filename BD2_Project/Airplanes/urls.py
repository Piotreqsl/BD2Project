from django.urls import path
from . import views


app_name = 'airports'

urlpatterns = [
    path('', views.AirportListView.as_view(), name='all'),
    path('airport/<int:pk>', views.AirportDetailView.as_view(), name='airport_detail'),
    path('airport/create', views.AirportCreateView.as_view(), name='airport_create'),
    path('airport/<int:pk>/update', views.AirportUpdateView.as_view(), name='airport_update'),
    path('airport/<int:pk>/delete', views.AirportDeleteView.as_view(), name='airport_delete'),
    
]