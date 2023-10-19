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


def show_details(request, id):
    member = Member.objects.get(id=id)
    template = loader.get_template('detail.html')
    context = {
        'member': member
    }
    return HttpResponse(template.render(context, request))


def toggle_bloque(request, id):
    member = Member.objects.get(pk=id)
    member.bloque = not member.bloque
    member.save()
    return redirect('show_details', id)


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
