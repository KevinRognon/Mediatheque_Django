# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .forms import MemberForm
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

    template = loader.get_template('show_medias_employee.html')
    context = {
        'books': books,
        'cds': cds,
        'dvds': dvds,
        'boardgames': boardgames
    }

    return HttpResponse(template.render(context, request))


def add_media(request):
    template = 'add_media.html'

    if request.method == "POST":
        type_media = request.POST.get('type_media')
        title = request.POST.get('title_media')
        author_field = request.POST.get('author_media')

        if type_media == "BOOK":
            book = Book(name=title, author=author_field, available=True)
            book.save()
        elif type_media == "CD":
            cd = Cd(name=title, artist=author_field, available=True)
            cd.save()
        elif type_media == "DVD":
            dvd = Dvd(name=title, realisator=author_field, available=True)
            dvd.save()
        elif type_media == "BOARDGAME":
            bg = BoardGame(name=title, creator=author_field)
            bg.save()

        return redirect("/employees/show-medias")

    return render(request, template)

def media_detail(request, media_type, media_id):


    template = loader.get_template("media_detail.html")

    if media_type == "book":
        media = Book.objects.get(id=media_id)
        type_media = media_type
    elif media_type == "cd":
        media = Cd.objects.get(id=media_id)
        type_media = media_type
    elif media_type == "dvd":
        media = Dvd.objects.get(id=media_id)
        type_media = media_type

    else:
        return HttpResponse("Type de média non reconnu.", status=400)

    context = {
        "media": media,
        "type_media": type_media
    }

    return HttpResponse(template.render(context, request))




def create_member(request):
    template = 'create_member.html'

    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            new_member = Member(firstname=first_name, lastname=last_name)
            new_member.save()

            return redirect('show_members')

    else:
        form = MemberForm()

    context = {
        'form': form
    }
    return render(request, template, context)


def delete_member(request, member_id):
    member = Member.objects.get(pk=member_id)

    if request.method == 'POST':
        member.delete()
        return redirect('show_members')

    return HttpResponse('Méthode non autorisée.')


