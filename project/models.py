from django.db import models
import uuid
# Create your models here.

# In project/models.py (assuming your app is named 'project')
class Client(models.Model):
    name = models.CharField(max_length=100)
    client_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Automatically generates unique UUID for security
    email = models.EmailField(unique=True)
    resources = models.JSONField() # To store resource-related information for calculations

    # Sustainability KPIs
    emissions = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Carbon emissions in tons
    energy_usage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Energy usage in kWh
    recycling = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Recycling rate in percentage
    commitments = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Commitments ratio in percentage
    
    # Loan details
    loan_rate = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)  # Current loan rate as a percentage
    loan_term = models.TextField(null=True, blank=True)  # AI-generated loan term
    
    def __str__(self):
        return self.name

