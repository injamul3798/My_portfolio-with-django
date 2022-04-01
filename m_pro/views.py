from django.shortcuts import render
from m_pro.models import Contact
from django.http import HttpResponse


#from .models import 


def index(request):
    return render (request, 'index.html')

def Myself(request):
    return render (request, 'Myself.html')


def contact(request):
    if request.method =='POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact.name = name
        contact.email = email
        contact.message = message
        contact.save()
        return HttpResponse("showdata.html")

    return render (request, 'Contact.html')

def showdata(request):
    data = Contact.objects.all()
    for i in data:
        print(i)
    return render (request, 'showdata.html',{'Contact':data})




 
 