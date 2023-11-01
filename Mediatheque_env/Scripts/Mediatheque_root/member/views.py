from django.shortcuts import render, loader
from django.http import HttpResponse
from Mediatheque_root.models import Book, Cd, Dvd, BoardGame

# Create your views here.

def show_medias(request):
    books = Book.objects.all().values()
    cds = Cd.objects.all().values()
    dvds = Dvd.objects.all().values()
    boardgames = BoardGame.objects.all().values()

    template = loader.get_template('show_medias.html')
    context = {
        'books': books,
        'cds': cds,
        'dvds': dvds,
        'boardgames': boardgames
    }

    return HttpResponse(template.render(context, request))
