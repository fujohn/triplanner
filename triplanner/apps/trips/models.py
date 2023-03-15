from django.db import models
from ..users.models import User

# Create your models here.
class TripManager(models.Manager):
    def trip_validator(self, postData):
        errors = {}
        if len(postData['destination']) < 3:
            errors['destination'] = 'Destination must be at least 3 characters'
        if postData['transportation'] not in ['car', 'public', 'walk']:
            errors['transportation'] = 'Please select a valid mode of transportation'
        if len(postData['description']) < 3:
            errors['description'] = 'Description must be at least 3 characters'
        return errors

class Trip(models.Model):
    destination = models.CharField(max_length=100)
    transportation = models.CharField(max_length=50)
    description = models.TextField()
    organizer = models.ForeignKey(User, related_name="trips", on_delete=models.CASCADE) # join?
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = TripManager()