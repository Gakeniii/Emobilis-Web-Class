from django.db import models

# Create your models here.
class Registration(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

    def __str__(self):
        return self.first_name

class Employee_details(models.Model):
    fullname = models.CharField(max_length=30)
    ID_no = models.CharField(max_length=8)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.fullname