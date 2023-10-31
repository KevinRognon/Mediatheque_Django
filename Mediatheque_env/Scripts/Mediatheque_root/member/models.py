from django.db import models


# Create your models here.


class Member(models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    bloque = models.BooleanField(null=False, default=False)
    nb_borrowed = models.IntegerField(default=0)

    def check_borrowed_nb(self):

        if self.nb_borrowed == 1 or self.nb_borrowed == 2:
            self.bloque = False
        elif self.nb_borrowed == 3:
            self.bloque = True
        else:
            self.bloque = False

        print(self.bloque)
