from django.db import models


# Create your models here.

class Member(models.Model):
    firstname = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    bloque = models.BooleanField(null=False, default=False)
    nb_borrowed = models.IntegerField(default=0)

    @property
    def borrowed_media(self):
        # Récupérer tous les médias empruntés
        books = list(self.book_set.all())
        cds = list(self.cd_set.all())
        dvds = list(self.dvd_set.all())

        # Fusionner les listes
        return books + cds + dvds

    def check_borrowed_nb(self):
        total_borrowed = len(self.borrowed_media)

        if 0 <= total_borrowed <= 2:
            self.bloque = False
        elif total_borrowed == 3:
            self.bloque = True

        # Mettre à jour le champ nb_borrowed
        self.nb_borrowed = total_borrowed
        self.save()
        print(self.bloque)
