from django.shortcuts import render, HttpResponse,redirect
from .models import *
from django.core.paginator import *
from django.contrib.auth import authenticate,logout,login

# Create your views here.

def home(request):
    images=Image.objects.all()
    category=Category.objects.all()
    paginator = Paginator(images, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data={'page_obj':page_obj,'category':category}
    return render(request,'home.html',data)

def category1(request,cid):
    category=Category.objects.get(pk=cid)
    images=Image.objects.filter(cat=category)
    category = Category.objects.all()
    paginator = Paginator(images, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data = {'page_obj': page_obj, 'category': category}
    return render(request,'home.html',data)

def aboutUs(request):
    return render(request,'aboutus.html')

def search(request):
    query=request.GET['query']
    title_images=Image.objects.filter(name__icontains=query)
    desc_images=Image.objects.filter(description__icontains=query)
    allimages=title_images.union(desc_images)
    if query == '':
        allimages=[]
    paginator = Paginator(allimages, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    data={'page_obj':page_obj}
    return render(request,'search.html',data)

def contact(request):
    return render(request,'contactus.html')



