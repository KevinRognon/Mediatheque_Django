from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=60)
    dateBorrow = models.DateField(null=True)
    available = models.BooleanField(null=False)
    borrower = models.ForeignKey('member.Member', on_delete=models.SET_NULL, null=True, blank=True)


class Cd(models.Model):
    name = models.CharField(max_length=100)
    artist = models.CharField(max_length=60)
    dateBorrow = models.DateField(null=True)
    available = models.BooleanField(null=False)
    borrower = models.ForeignKey('member.Member', on_delete=models.SET_NULL, null=True, blank=True)


class Dvd(models.Model):
    name = models.CharField(max_length=100)
    realisator = models.CharField(max_length=60)
    dateBorrow = models.DateField(null=True)
    available = models.BooleanField(null=False)
    borrower = models.ForeignKey('member.Member', on_delete=models.SET_NULL, null=True, blank=True)


class BoardGame(models.Model):
    name = models.CharField(max_length=100)
    creator = models.CharField(max_length=60)

