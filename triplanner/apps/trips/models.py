from django.db import models
from ..users.models import User

# Create your models here.
class Trip(models.Model):
    destination = models.CharField(max_length=100)
    transportation = models.CharField(max_length=50)
    description = models.TextField()
    organizer = models.ForeignKey(User, related_name="trips", on_delete=models.CASCADE) # join?
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)