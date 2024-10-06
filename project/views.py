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
#################################    CLIENT DETAILS   #######################################
############################################################################################


def client_details(request, client_id):
    # Fetch the client object using the client_id
    client = get_object_or_404(Client, client_id=client_id)

    # Prepare the KPI data to send to OpenAI
    kpi_data = {
        'emissions': client.emissions,
        'recycling': client.recycling,
        'commitments': client.commitments,
    }
    
    # Generate loan terms using OpenAI
    loan_terms = generate_loan_terms(kpi_data)

    # Debugging: Print the generated loan terms
    print(f"Generated Loan Terms: {loan_terms}")

    # Check if loan_terms is not None or empty before saving
    if loan_terms:
        # Save the generated loan terms to the client model
        client.loan_term = loan_terms
        client.save()
        print("Loan terms saved successfully.")
    else:
        print("No loan terms generated.")

    # Render the client details template and explicitly pass the loan_term
    return render(request, 'project/client_details.html', {
        'client': client,
        'loan_term': client.loan_term  # Pass the loan term directly to the template
    })
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



from bson import ObjectId

def submit2(request):
    if request.method == 'POST':
        # Get client data from session
        client_data = request.session.get('client_data')

        if not client_data:
            return HttpResponse("Client data not found.")

        # Get sustainability-related form data
        reduce_water = request.POST.get('reduce_water', 'off') == 'on'
        reduce_water_value = request.POST.get('reduce_water_value')
        reduce_electricity = request.POST.get('reduce_electricity', 'off') == 'on'
        reduce_electricity_value = request.POST.get('reduce_electricity_value')

        # Update the session data with new values
        client_data.update({
            'reduce_water': reduce_water,
            'reduce_water_value': reduce_water_value,
            'reduce_electricity': reduce_electricity,
            'reduce_electricity_value': reduce_electricity_value
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

    # Pass all client data to the template
    return render(request, 'project/confirmation.html', {'client_data': client_data})
