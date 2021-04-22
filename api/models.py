from django.db import models

# Create your models here.

class UserAccess(models.Model):
    firstName  = models.CharField(max_length=100)
    middleName = models.CharField(max_length=100)
    lastName   = models.CharField(max_length=100)
    email      = models.EmailField(max_length = 254)
    password   =  models.CharField(max_length=20)

    def __str__(self):
        return self.firstName + self.lastName