import openai
from django.conf import settings

# Set OpenAI API key
openai.api_key = settings.OPENAI_API_KEY

def generate_loan_terms(kpi_data):
    if kpi_data:
        try:
            # Create dynamic message content based on the selected KPIs
            kpi_message = []
            if kpi_data.get('reduce_water') is not None:
                kpi_message.append(f"Reduce Water by {kpi_data['reduce_water_value']}%")
            if kpi_data.get('reduce_electricity') is not None:
                kpi_message.append(f"Reduce Electricity by {kpi_data['reduce_electricity_value']}%")
            if kpi_data.get('reduce_waste') is not None:
                kpi_message.append(f"Reduce Waste by {kpi_data['reduce_waste_value']}%")
            if kpi_data.get('energy_efficient_lightbulbs') is not None:
                kpi_message.append(f"Switch to Energy Efficient Lightbulbs by {kpi_data['energy_efficient_lightbulbs_value']}%")
            if kpi_data.get('reduce_co2') is not None:
                kpi_message.append(f"Reduce CO2 emissions by {kpi_data['reduce_co2_value']}%")

            # Join KPI data into a message
            kpi_message = "; ".join(kpi_message)

            # Use OpenAI's ChatCompletion API to generate loan terms
            completion = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a financial assistant helping to create loan terms based on sustainability data."},
                    {
                        "role": "user",
                        "content": f"Here is the KPI data: {kpi_message}. Generate a loan term recommendation."
                    }
                ]
            )
            
            # Return the generated loan term from the response
            return completion['choices'][0]['message']['content']
        
        except Exception as e:
            # Handle any errors that occur during the API call
            print(f"Error with OpenAI: {e}")
            return "Unable to generate loan terms at this time."
    
    return None
