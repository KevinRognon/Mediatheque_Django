
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Employe
from 


def employee(request):
    employees = Employe.objects.all().values
    template = loader.get_template('employe.html')
    context = {
        'employees': employees
    }
    return HttpResponse(template.render(context, request))



def show_members(request):
    members = Member.objects.all().values()
