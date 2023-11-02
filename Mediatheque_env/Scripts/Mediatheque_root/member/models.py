from django.db import models
from datetime import date, timedelta


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

    def has_overdue_items(self):
        today = date.today()
        one_week_ago = today - timedelta(days=7)

        # Vérifiez les livres
        if self.book_set.filter(dateBorrow__lt=one_week_ago).exists():
            return True

        # Vérifiez les CDs
        if self.cd_set.filter(dateBorrow__lt=one_week_ago).exists():
            return True

        # Vérifiez les DVDs
        if self.dvd_set.filter(dateBorrow__lt=one_week_ago).exists():
            return True

        return False