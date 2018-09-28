# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render,get_object_or_404

# Create your views here.
def home(request):
    images = Image.objects.all()
    categories = Category.objects.all()
    return render(request,'home.html',locals())

def search(request):
    searchstring=request.POST['search']
    images=Image.search_image(searchstring)
    name=searchstring
    title=name
    return render(request,'results.html',locals())

def getcat(request,catid):
    category=get_object_or_404(Category,pk = catid)
    title=category.Name
    name=category.Name
    images=category.images.all()
    return render(request,'results.html',locals())
