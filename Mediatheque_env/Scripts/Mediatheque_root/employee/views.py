
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Employe
from member.models import Member
from Mediatheque_root.models import Book, Cd, Dvd, BoardGame




def employee(request):
    employees = Employe.objects.all().values
    template = loader.get_template('employe.html')
    context = {
        'employees': employees
    }
    return HttpResponse(template.render(context, request))



def show_members(request):
    members = Member.objects.all().values()
    template = loader.get_template('show_members.html')
    context = {
        'members': members
    }
    return HttpResponse(template.render(context, request))


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


def create_member(request):
    template = loader.get_template('create_member.html')
    return HttpResponse(template.render)

