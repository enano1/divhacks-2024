import openai
from django.conf import settings

# Set OpenAI API key
openai.api_key = settings.OPENAI_API_KEY

def generate_loan_terms(kpi_data, business_name, loan_amount):
    if kpi_data:
        try:
            # Create dynamic message content based on the selected KPIs
            kpi_message = []
            if kpi_data.get('reduce_water') is not False:
                kpi_message.append(f"Reduce Water by {kpi_data['reduce_water_value']}%")
            if kpi_data.get('reduce_electricity') is not False:
                kpi_message.append(f"Reduce Electricity by {kpi_data['reduce_electricity_value']}%")
            if kpi_data.get('reduce_waste') is not False:
                kpi_message.append(f"Reduce Waste by {kpi_data['reduce_waste_value']}%")
            if kpi_data.get('energy_efficient_lightbulbs') is not False:
                kpi_message.append(f"Switch to Energy Efficient Lightbulbs by {kpi_data['energy_efficient_lightbulbs_value']}%")
            if kpi_data.get('reduce_co2') is not False:
                kpi_message.append(f"Reduce CO2 emissions by {kpi_data['reduce_co2_value']}%")

            # Join KPI data into a message
            kpi_message = "; ".join(kpi_message)
            print(kpi_message)
            # Use OpenAI's ChatCompletion API to generate loan terms
            completion = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a bank analyst helping to create loan terms based on sustainability data."},
                    {
                        "role": "user",
                        
                        "content": f'''
                        You work for a bank and are in charge of setting the terms for sustainably linked loans. You receive applications with a business's loan request, time frame (in periods), and KPIs that they commit to reaching by the end of the time frame. The current market interest rate on loans is 6%. By attaching the loan to these KPIs the businesses get a lower rate if they are successful in reaching their sustainability targets. The KPIs will be tracked quarterly in regards to the loan (i.e. 4 times during the loan's period)

                        Your goal is, based on the provided targets, identify a fair interest rate. You also need to denote a percentage increase in the interest rate for each quarter if they miss one, two, or three of the targets. The expected output is going to a database and needs a specific format. You are only to respond in this format, do not explain your answer. Here are some examples. The explanation is not going into the database but is for your reference:

                        Input
                        Reduce Pollution by 70%; Switch to Energy Efficient Lightbulbs by 50%; Reduce Water emissions by 95%

                        Output (without saying output)
                        Rate:2%;increasemiss1:0.3%;increasemiss2:0.6%;increasemiss3:0.7%

                        Explanation
                        These targets are pretty difficult to reach so the rate is very low. However missing targets has a large effect on the rate.

                        Input
                        Reduce Water by 1%; Switch to Energy Efficient Lightbulbs by 13%; Reduce CO2 emissions by 21%

                        Output (without saying output)
                        Rate:4.6%;increasemiss1:0.05%;increasemiss2:0.1%;increasemiss3:0.125%

                        Explanation
                        These targets are relatively easy to attain, especially the water one so the rate is quite low. The quarterly increases in rate if 1, 2, 3 targets are missed are pretty proportional.

                        Try it for this example:
                        Input: {kpi_message}


                    '''
                    
                    }
                ]
            )
            rate = completion['choices'][0]['message']['content']
            # Return the generated loan term from the response
            completion = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are a bank lawyer helping to create loan terms based on sustainability data."},
                        {
                            "role": "user",
                            
                            "content": f'''
                            You are working for the legal team of a bank. Your job is to generate a legal sustainability-linked loan contract given a loan amount, business name, interest rate breakdown and kpi indicators.

                            The interest rate breakdown is given as Rate:4%;increasemiss1:0.1%;increasemiss2:0.2%;increasemiss3:0.3%. This is tied with kpi indicators that will be given like Reduce Water by 15%; Reduce Electricity by 30%; Switch to Energy Efficient Lightbulbs by 13%.

                            Interest rate starts as a fix rate. The company's progress towards reaching the kpis is evaluated on a quarter basis in terms of the loan's period (in months). This means that the period is split into 4 and each of the indicators is split in the 4. If the business achieves each of the 3 indicators in a quarter the interest rate does not increase. If it misses one indicator in a quarter the interest rate increases by interestrate1 that quarter and for the rest of the loan's period. If it misses two indicators the rate increases by interestrate2 and so on. 
                            Use "\ n" for newlines without the space
                            Try it for this example:
                            Business Name: {business_name}
                            Loan Amount: {loan_amount}
                            Rates: {rate}
                            KPIs: {kpi_message}

                        '''
                        
                        }
                    ]
                )
                
                # Return the generated loan term from the response
            return rate, completion['choices'][0]['message']['content']
        except Exception as e:
            # Handle any errors that occur during the API call
            print(f"Error with OpenAI: {e}")
            return "Unable to generate loan terms at this time."

