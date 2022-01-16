from curses.ascii import HT
from django.http import HttpResponse 

# Create your views here.

def homePageView(request):
    return HttpResponse("Hello, World!")
    