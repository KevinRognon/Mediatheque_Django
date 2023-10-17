
# Create your views here.
from django.http import HttpResponse
from django.template import loader


def employee(request):
    template = loader.get_template('employe.html')
    return HttpResponse(template.render())

