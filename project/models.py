from django.db import models



class Client(models.Model):
    name = models.CharField(max_length=100, default="")
    email = models.EmailField(default="")
    revenue = models.IntegerField(default=0)
    description = models.TextField(default="")

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

    loan_terms = models.TextField(null=True, blank=True)  # New field to store loan terms

    def __str__(self):
        return self.name
