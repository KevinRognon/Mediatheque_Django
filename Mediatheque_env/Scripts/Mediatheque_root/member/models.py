from django.db import models

# Create your models here.


class Member(models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    bloque = models.BooleanField(null=False, default=False)
    nb_borrowed = models.IntegerField(default=0)

