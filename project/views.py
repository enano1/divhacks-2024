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
def dashboard(request):
    '''
    View for the home page
    '''

    template_name = 'project/dashboard.html'

    return render(request, template_name)
def application(request):
    '''
    View for the home page
    '''

    template_name = 'project/application.html'

    return render(request, template_name)
def kpichooser(request):
    '''
    View for the home page
    '''

    template_name = 'project/kpichooser.html'

    return render(request, template_name)
def loantracker(request):
    '''
    View for the home page
    '''

    template_name = 'project/loantracker.html'

    return render(request, template_name)
