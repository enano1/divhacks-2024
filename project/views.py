from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from .models import *

def home(request):
    '''
    View for the home page
    '''

    template_name = 'project/home.html'

    return render(request, template_name)
