# Url Patterns for the project!!

from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('client/<uuid:client_id>/', views.client_details, name='client_details'),

]