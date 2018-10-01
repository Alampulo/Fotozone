from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return render(request, 'base.html')

def home(request):

    message = 'hiiiii'
    return render(request, 'welcome.html')