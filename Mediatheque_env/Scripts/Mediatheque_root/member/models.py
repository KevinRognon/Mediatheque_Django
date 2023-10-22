from django.db import models

# Create your models here.


class Member(models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    bloque = models.BooleanField(null=False, default=False)
    nb_borrowed = models.IntegerField(default=0)

    def check_borrowed_nb(self):


        match self.nb_borrowed:
            case 2 | 1:
                self.bloque = False
            case 3:
                self.bloque = True
            case _:
                self.bloque = False

        print(self.bloque)


