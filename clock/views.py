from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Data

# Create your views here.
def downCounter(request):
    return render(request,'downCounter.html')

def index(request):
    if request.is_ajax():
        if request.POST.get('name') and request.POST.get('pin'):
            post=Data()
            post.name=request.POST.get('name')
            post.pin=request.POST.get('pin')
            post.save()
            return JsonResponse({
                    'message': 'success'
                })
        else:
            return JsonResponse({
                'message': 'failed'
            })
    return render(request,'index.html')

def counter(request):
    return render(request,'counter.html')
