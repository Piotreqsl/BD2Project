from django.urls import re_path
from airlines import views

urlpatterns = [
    re_path(r'^airlines/$', views.airline_list),
    re_path(r'^airlines/(?P<pk>[0-9]+)$', views.airline_detail),
]