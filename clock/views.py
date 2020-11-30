from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Data

# Create your views here.
def downCounter(request):
    return render(request,'downCounter.html')

def index(request):
    return render(request,'index.html')

def counter(request):
    return render(request,'counter.html')

def save(request):
    if request.method=='POST':
        if request.POST.get('name') and request.POST.get('password'):
            post=Data()
            post.name=request.POST.get('name')
            post.pin=request.POST.get('password')
            post.save()
        return HttpResponse("sucess")
    else:
        return HttpResponse('problem')