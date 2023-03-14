from django.db import models
import re

# Create your models here.
class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        if len(postData['name']) < 3:
            errors['name'] = 'Name must be at least 3 characters'

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = "Invalid email address"

        if len(postData['password']) < 8:
            errors['password'] = 'Password must be at least 8 characters'

        if postData['password'] != postData['confirm_pw']:
            errors['confirm_pw'] = 'Passwords do not match'
        return errors
    

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password_hash = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager() # validation (see above)