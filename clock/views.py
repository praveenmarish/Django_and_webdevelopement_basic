from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def downCounter(request):
    return render(request,'downCounter.html')

def index(request):
    return render(request,'index.html')

def counter(request):
    return render(request,'counter.html')