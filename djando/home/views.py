from django.shortcuts import render , HttpResponse

def index(request):
    context = {"variable":"this is sent"
    }
    return render(request,'index.html',context)
    #return HttpResponse("This is homepage")
def b.fashion(request):
    return render(request,'BOY FASHION.html')
def feeding(request):
    return render(request,'FEEDING.html')
def g.fashion(request):
    return render(request,'GIRL FASHION.html')
def toys(request):
    return render(request,'TOYS.html')
def footwear(request):
    return render(request,'FOOTWEAR.html')
def contact(request):
    return render(request,'CONTACT US.html')
def contact(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'index.html')