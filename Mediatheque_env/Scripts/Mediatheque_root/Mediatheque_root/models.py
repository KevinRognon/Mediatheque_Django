from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=60)
    dateBorrow = models.DateField(null=True)
    available = models.BooleanField(null=False)
    borrower = models.CharField(max_length=60)


class Cd(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=60)
    dateBorrow = models.DateField(null=False)
    available = models.BooleanField(null=False)
    borrower = models.CharField(max_length=60)


class Dvd(models.Model):
    name = models.CharField(max_length=100)
    realisator = models.CharField(max_length=60)
    dateBorrow = models.DateField(null=False)
    available = models.BooleanField(null=False)
    borrower = models.CharField(max_length=60)


class BoardGame(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=60)

