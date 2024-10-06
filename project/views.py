from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
from .utils import generate_loan_terms
from django.http import HttpResponse
# import bson
# from .db import db  # Import the db connection

############################################################################################
#################################   HOME    #######################################
############################################################################################

def home(request):

    return render(request, 'project/home.html')


############################################################################################
#################################    DASHBOARD    #######################################
############################################################################################

def dashboard(request):
    '''
    View for the home page
    '''

    template_name = 'project/dashboard.html'

    return render(request, template_name)

############################################################################################
#################################    APPLICATION    #######################################
############################################################################################

def application(request):
    '''
    View for the home page
    '''

    template_name = 'project/application.html'

    return render(request, template_name)

############################################################################################
#################################    KPI CHOOSER    #######################################
############################################################################################

def kpichooser(request):
    '''
    View for the home page
    '''

    template_name = 'project/kpichooser.html'

    return render(request, template_name)

############################################################################################
#################################    LOAN TRACKER    #######################################
############################################################################################

def loantracker(request):
    '''
    View for the home page
    '''

    template_name = 'project/loantracker.html'

    return render(request, template_name)



############################################################################################
#################################    SUBMIT    #############################################
############################################################################################


def submit1(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        revenue = request.POST.get('revenue')
        description = request.POST.get('description')

        # Validation check for required fields
        if not all([name, email, revenue, description]):
            return render(request, 'project/application.html', {
                'error': 'Please fill in all the required fields.'
            })

        # Store client data in the session
        request.session['client_data'] = {
            'name': name,
            'email': email,
            'revenue': revenue,
            'description': description
        }

        return redirect('kpichooser')

    return render(request, 'project/application.html')


from .models import Client
from django.shortcuts import redirect, render, HttpResponse
from .utils import generate_loan_terms

def submit2(request):
    if request.method == 'POST':
        # Get client data from session
        client_data = request.session.get('client_data')

        if not client_data:
            return HttpResponse("Client data not found.")

        # Get sustainability-related form data and handle empty values for numeric fields
        reduce_water = request.POST.get('reduce_water', 'off') == 'on'
        reduce_water_value = request.POST.get('reduce_water_value') or 0  # Default to 0 if empty
        reduce_electricity = request.POST.get('reduce_electricity', 'off') == 'on'
        reduce_electricity_value = request.POST.get('reduce_electricity_value') or 0
        reduce_waste = request.POST.get('reduce_waste', 'off') == 'on'
        reduce_waste_value = request.POST.get('reduce_waste_value') or 0
        energy_efficient_lightbulbs = request.POST.get('energy_efficient_lightbulbs', 'off') == 'on'
        energy_efficient_lightbulbs_value = request.POST.get('energy_efficient_lightbulbs_value') or 0
        reduce_co2 = request.POST.get('reduce_co2', 'off') == 'on'
        reduce_co2_value = request.POST.get('reduce_co2_value') or 0

        # Update the session data with new values
        client_data.update({
            'reduce_water': reduce_water,
            'reduce_water_value': reduce_water_value,
            'reduce_electricity': reduce_electricity,
            'reduce_electricity_value': reduce_electricity_value,
            'reduce_waste': reduce_waste,
            'reduce_waste_value': reduce_waste_value,
            'energy_efficient_lightbulbs': energy_efficient_lightbulbs,
            'energy_efficient_lightbulbs_value': energy_efficient_lightbulbs_value,
            'reduce_co2': reduce_co2,
            'reduce_co2_value': reduce_co2_value
        })

        # Store updated client data in session
        request.session['client_data'] = client_data

        # Redirect to the confirmation page
        return redirect('confirmation')

    return render(request, 'project/kpichooser.html')


def confirmation(request):
    # Retrieve client data from the session
    client_data = request.session.get('client_data')

    if not client_data:
        return HttpResponse("No client data found.")

    # Prepare KPI data for the loan terms generation
    kpi_data = {
        'reduce_water': client_data.get('reduce_water'),
        'reduce_water_value': client_data.get('reduce_water_value'),
        'reduce_electricity': client_data.get('reduce_electricity'),
        'reduce_electricity_value': client_data.get('reduce_electricity_value'),
        'reduce_waste': client_data.get('reduce_waste'),
        'reduce_waste_value': client_data.get('reduce_waste_value'),
        'energy_efficient_lightbulbs': client_data.get('energy_efficient_lightbulbs'),
        'energy_efficient_lightbulbs_value': client_data.get('energy_efficient_lightbulbs_value'),
        'reduce_co2': client_data.get('reduce_co2'),
        'reduce_co2_value': client_data.get('reduce_co2_value')
    }

    # Generate loan terms using OpenAI
    loan_terms = generate_loan_terms(kpi_data)

    # Pass the client data and generated loan terms to the template
    return render(request, 'project/confirmation.html', {
        'client_data': client_data,
        'loan_terms': loan_terms  # Include the generated loan terms
    })
