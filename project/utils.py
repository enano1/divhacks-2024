from openai import OpenAI
from django.conf import settings
import openai
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_loan_terms(kpi_data):
    try:
        completion = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a financial assistant helping to create loan terms based on sustainability data."},
                {
                    "role": "user",
                    "content": f"Here is the KPI data: Emissions: {kpi_data['emissions']} tons, Recycling rate: {kpi_data['recycling']}%, Commitments ratio: {kpi_data['commitments']}%. Generate a loan term recommendation."
                }
            ]
        )
        
        # Print the entire OpenAI response for debugging
        print(completion)

        # Return the generated loan term
        return completion.choices[0].message.content
    except openai.error.AuthenticationError as e:
        print(f"Authentication Error: {e}")
        return "Invalid API key. Please check your OpenAI API key."
    except Exception as e:
        print(f"Error with OpenAI: {e}")
        return "Unable to generate loan terms at this time."
