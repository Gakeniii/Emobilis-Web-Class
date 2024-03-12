
from django.db import models

# class Registration(models.Model):
#     first_name = models.CharField(max_length=10)
#     last_name = models.CharField(max_length=10)
#     email = models.EmailField()
#     password = models.CharField(max_length=10)
#
#     def __str__(self):
#         return self.first_name

class Profile(models.Model):
    FirstName = models.CharField(max_length=10)
    LastName = models.CharField(max_length=10)
    age = models.IntegerField()
    DOB = models.DateField()

    def __str__(self):
        return self.FirstName
