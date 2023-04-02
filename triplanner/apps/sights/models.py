from django.db import models
from ..users.models import User
from ..trips.models import Trip

# Create your models here.
class SightManager(models.Manager):
    def sight_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = 'Sight name must be at least 3 characters'
        if len(postData['day']) < 1:
            errors['day'] = 'Please enter a valid number for Trip Day'
        elif int(postData['day']) < 0:
            errors['day'] = 'Day must be greater than 0'
        if len(postData['order']) < 1:
            errors['order'] = 'Please enter a valid number for Event Order'
        elif int(postData['order']) < 0:
            errors['order'] = 'Order must be greater than 0'
        if len(postData['duration']) < 1:
            errors['duration'] = 'Please enter a valid number for Duration'
        elif int(postData['duration']) < 10:
            errors['duration'] = 'Duration must be at least 10 minutes'
        if len(postData['description']) < 3:
            errors['description'] = 'Description must be at least 3 characters'
        return errors

class Sight(models.Model):
    name = models.CharField(max_length=100)
    google_search_name = models.CharField(max_length=255) # trigger if null then do no include commute time between connecting events
    day = models.IntegerField()
    order = models.IntegerField()
    duration = models.IntegerField()
    description = models.TextField()
    creator = models.ForeignKey(User, related_name="sights", on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, related_name="sights", on_delete=models.CASCADE)
    previous = models.OneToOneField('self', null=True, blank=True, related_name='next', on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = SightManager()