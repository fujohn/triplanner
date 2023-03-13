from django.db import models
from ..users.models import User
from ..trips.models import Trip

# Create your models here.
class Sight(models.Model):
    name = models.CharField(max_length=100)
    day = models.IntegerField()
    order = models.IntegerField()
    duration = models.IntegerField()
    description = models.TextField()
    creator = models.ForeignKey(User, related_name="sights", on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, related_name="sights", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)