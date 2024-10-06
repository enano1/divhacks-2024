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
        # Get the form data from the POST request
        business_name = request.POST.get('businessname')
        business_email = request.POST.get('businessemail')
        business_owner = request.POST.get('businessowner')
        tin = request.POST.get('tin')
        business_history = request.POST.get('businesshistory')
        ownership_structure = request.POST.get('ownershipstructure')
        loan_amount = request.POST.get('loanamount')
        loan_timeframe = request.POST.get('loantimeframe')
        purpose = request.POST.get('purpose')
        revenue = request.POST.get('revenue')

        # Validation check for required fields
        if not all([business_name, business_email, business_owner, tin, business_history, ownership_structure, loan_amount, loan_timeframe, purpose, revenue]):
            return render(request, 'project/application.html', {
                'error': 'Please fill in all the required fields.'
            })

        # Create a Client object and save it to the database
        client = Client.objects.create(
            user=request.user,  # Associate with the logged-in user
            business_name=business_name,
            business_email=business_email,
            business_owner=business_owner,
            tax_identification_number=tin,
            business_history=business_history,
            ownership_structure=ownership_structure,
            loan_amount=loan_amount,
            loan_timeframe=loan_timeframe,
            purpose=purpose,
            revenue=revenue
        )

        # Store the client ID in session (for later reference)
        request.session['client_id'] = client.id

        return redirect('kpichooser')  # Redirect to the next view

    return render(request, 'project/application.html')


from .models import Client
from django.shortcuts import redirect, render, HttpResponse
from .utils import generate_loan_terms

def submit2(request):
    if request.method == 'POST':
        # Use filter() to fetch all matching clients for the logged-in user
        clients = Client.objects.filter(user=request.user)
        
        if not clients.exists():
            return HttpResponse("No clients found for the user.")
        
        # Update client data with the new values
        for client in clients:
            client.reduce_water = request.POST.get('reduce_water', 'off') == 'on'
            client.reduce_water_value = request.POST.get('reduce_water_value') or 0
            client.reduce_electricity = request.POST.get('reduce_electricity', 'off') == 'on'
            client.reduce_electricity_value = request.POST.get('reduce_electricity_value') or 0
            client.reduce_waste = request.POST.get('reduce_waste', 'off') == 'on'
            client.reduce_waste_value = request.POST.get('reduce_waste_value') or 0
            client.energy_efficient_lightbulbs = request.POST.get('energy_efficient_lightbulbs', 'off') == 'on'
            client.energy_efficient_lightbulbs_value = request.POST.get('energy_efficient_lightbulbs_value') or 0
            client.reduce_co2 = request.POST.get('reduce_co2', 'off') == 'on'
            client.reduce_co2_value = request.POST.get('reduce_co2_value') or 0

            # Save the client instance
            client.save()

        # Redirect to the confirmation page (pass the first client ID for simplicity)
        return redirect('confirmation', client_id=clients.first().id)

    return render(request, 'project/kpichooser.html')


def confirmation(request):
    # Fetch the first client for the logged-in user
    client = Client.objects.filter(user=request.user).first()

    if not client:
        return HttpResponse("No client data found.")

    # Directly access client data
    kpi_data = {
        'reduce_water': client.reduce_water,
        'reduce_water_value': client.reduce_water_value,
        'reduce_electricity': client.reduce_electricity,
        'reduce_electricity_value': client.reduce_electricity_value,
        'reduce_waste': client.reduce_waste,
        'reduce_waste_value': client.reduce_waste_value,
        'energy_efficient_lightbulbs': client.energy_efficient_lightbulbs,
        'energy_efficient_lightbulbs_value': client.energy_efficient_lightbulbs_value,
        'reduce_co2': client.reduce_co2,
        'reduce_co2_value': client.reduce_co2_value,
    }

    # Generate loan terms using OpenAI (adjust according to your logic)
    loan_terms, loan_contract = generate_loan_terms(kpi_data, client.business_name, client.loan_amount)
    client.loan_terms = loan_contract

    # Split the loan terms and update the client model
    terms = loan_terms.split(';')
    client.loan_rate = terms[0].split(':')[1]
    client.loan_increasemiss1 = terms[1].split(':')[1]
    client.loan_increasemiss2 = terms[2].split(':')[1]
    client.loan_increasemiss3 = terms[3].split(':')[1]
    client.save()

    # Pass the actual client model data and generated loan terms to the template
    return render(request, 'project/confirmation.html', {
        'client': client,  # Pass the single client
        'loan_contract': loan_contract,
    })


####### LOGIN AND LOGOUT ########

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log in the user after registration
            return redirect('dashboard')  # Redirect to dashboard instead of profile
    else:
        form = RegisterForm()
    return render(request, 'project/register.html', {'form': form})

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages  # For flash messages
from django.http import HttpResponse

def custom_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # Log the user in
            return redirect('dashboard')  # Redirect to your dashboard or another page
        else:
            messages.error(request, "Invalid username or password")  # Show error message
    
    return render(request, 'project/loginpage.html')  # Use your custom template

############### current loans ################

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Client

@login_required
def current_loans(request):
    # Fetch all loans associated with the logged-in user
    loans = Client.objects.filter(user=request.user)

    # Pass the loans to the template
    return render(request, 'project/currentloans.html', {'loans': loans})

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)  # This will log the user out by clearing the session
    return redirect('loginpage')  # Redirect to login page or another page after logging out

