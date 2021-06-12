from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import destination , Contact
from django.contrib import messages
from django.contrib.auth.models import User, auth

def index(request):
    dests=destination.objects.all()
    return render(request, 'index.html',{'dests':dests})

def abc(request):
    if request.method=='POST':
        destin=request.POST['destin']
        ca=request.session.get('ca')
        if ca:
            ca[destin]=1
        else:
            ca={}
            ca[destin]=1
        request.session['ca']=ca
        print(ca)
        return redirect('http://127.0.0.1:8000/home1')



def home1(request):
    dests=destination.objects.all()
    return render(request, 'home1.html',{'dests':dests})

def home2(request):
    
    return redirect('home')

def your_desti(request):
    
    return render(request,'your_destination.html')

def get_prod(ids):
    return destination.objects.filter(id__in=ids)
    

def productView(request, myid):
    # fetch product using id
    dests=destination.objects.filter(id=myid)
    return render (request,'productview.html',{'dests':dests[0]})


def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        query=request.POST['query']
        contact=Contact(name=name, email=email, phone=phone, query=query)
        contact.save()
        messages.info(request,'your description has been saved')
        return redirect('contact')
    return render(request,'contact.html')


    

    