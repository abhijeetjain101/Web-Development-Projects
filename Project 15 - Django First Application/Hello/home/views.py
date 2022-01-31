from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "variable1": "Jeet is great",
        "variable2": "Devavrat is great"
    }
    messages.success(request, "this is a test message")
    return render(request, 'index.html', context)
    # return HttpResponse("this is home page")

def aboutus(request):
    # return HttpResponse("this is about page")
    return render(request, 'aboutus.html')

def services(request):
    # return HttpResponse("this is services")
    return render(request, 'services.html')

def contact(request):
    # return HttpResponse("this is contact page")
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        # date = request.POST.get(datetime.today())
        contact = Contact(name= name, email=email, phone=phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request, 'contact.html')