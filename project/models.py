from django.db import models
import uuid
# Create your models here.

# In project/models.py (assuming your app is named 'project')
class Client(models.Model):
    name = models.CharField(max_length=100)
    client_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # Automatically generates unique UUID for security
    email = models.EmailField(unique=True)
    resources = models.JSONField() # To store resource-related information for calculations

    def __str__(self):
        return self.name
