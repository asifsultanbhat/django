from django.shortcuts import render , HttpResponse

def index(request):
    context = {"variable":"this is sent"
    }
    return render(request,'index.html',context)
    #return HttpResponse("This is homepage")
def contact(request):
    return HttpResponse("This contact page")
