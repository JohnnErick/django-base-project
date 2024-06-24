from django.http import HttpResponse
from django.template import loader

def singlepage(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())