from django.shortcuts import render , HttpResponse
from datetime import datetime
from home.models import Contact

def index(request):
    return render(request,'index.html')
def boysfashion(request):
    return render(request,'BOY FASHION.html')
def feeding(request):
    return render(request,'FEEDING.html')
def girlsfashion(request):
    return render(request,'GIRL FASHION.html')
def toys(request):
    return render(request,'TOYS.html')
def footwear(request):
    return render(request,'FOOTWEAR.html')
def contact(request):
    if request.method == "post":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = contact(name=name,email=email,phone=phone,desc=desc,date=datetime.today())
        contact.save()
    return render(request,'CONTACT US.html')
def HEALTH(request):
    return render(request,'HEALTH.html')
def ACCESSORY(request):
    return render(request,'ACCESSORY.html')
def DIAPERING(request):
    return render(request,'DIAPERING.html')
    
        