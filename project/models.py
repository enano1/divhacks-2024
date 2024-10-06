from django.contrib.auth.models import User
from django.db import models

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Associate Client with a User
    business_name = models.CharField(max_length=100, default="")  # matches 'businessname' input
    business_email = models.EmailField(default="")  # matches 'businessemail' input
    business_owner = models.CharField(max_length=100, default="")  # matches 'businessowner' input
    tax_identification_number = models.CharField(max_length=20, default="")  # matches 'tin' input
    business_history = models.TextField(default="")  # matches 'businesshistory' input
    ownership_structure = models.TextField(default="")  # matches 'ownershipstructure' input
    loan_amount = models.IntegerField(default=0)  # matches 'loanamount' input
    loan_timeframe = models.IntegerField(default=0)  # matches 'loantimeframe' input
    purpose = models.TextField(default="")  # matches 'purpose' textarea
    revenue = models.IntegerField(default=0)  # matches 'revenue' input


    # Sustainability KPIs fields
    reduce_water = models.BooleanField(default=False)
    reduce_water_value = models.PositiveIntegerField(null=True, blank=True)

    reduce_electricity = models.BooleanField(default=False)
    reduce_electricity_value = models.PositiveIntegerField(null=True, blank=True)

    reduce_waste = models.BooleanField(default=False)
    reduce_waste_value = models.PositiveIntegerField(null=True, blank=True)

    energy_efficient_lightbulbs = models.BooleanField(default=False)
    energy_efficient_lightbulbs_value = models.PositiveIntegerField(null=True, blank=True)

    reduce_co2 = models.BooleanField(default=False)
    reduce_co2_value = models.PositiveIntegerField(null=True, blank=True)

    loan_terms = models.TextField(null=True, blank=True)  # Field to store loan terms

    def __str__(self):
        return self.name
