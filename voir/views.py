from django.http import HttpResponse
from django.shortcuts import render
from voir.models import *
# Create your views here.
def home(request):
    return render(request, 'index.html')

def listing(request):

    from django.template import Template, Context

    objects = Task.objects.all().order_by('due_date')

    template = Template(' {% for elem in objects %} {{elem}} <br/> {% endfor %} ')

    print(str(template))
    context = Context({'objects': objects})
    print(str(template.render(context)))

    return HttpResponse(template.render(context))

def list(request):
    task = Task.objects.all().order_by('due_date')

    return render(request, 'listing.html', {'tasks':task})