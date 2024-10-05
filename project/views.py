from django.shortcuts import render, get_object_or_404
from .models import Client
from .utils import generate_loan_terms

def home(request):

    return render(request, 'project/home.html')

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
