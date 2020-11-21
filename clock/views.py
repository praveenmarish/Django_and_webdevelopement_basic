from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def index(request):
    if request.method=='POST':
        val=request.POST['values']
    else:
        val=0
    return render(request,'counter.html',{'counter':val})

def count(request):
    val=request.POST['values']
    return render(request,'counter.html',{'counter':val})

def run(request):
    return HttpResponse('runing')