from django.db import models

# Create your models here.


class Employe(models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    phone_number = models.IntegerField(null=True)
    joined_date = models.DateField(null=True)

