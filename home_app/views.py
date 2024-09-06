import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home(request):
    now = datetime.datetime.now()
    html = "<html><body>This is appliation 2 It is now %s.</body></html>" % now
    return HttpResponse(html)
     