from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Data, MultipleImageUpload

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
                    'message': 'success',
                })
        else:
            return JsonResponse({
                'message': 'failed'
            })
    return render(request,'index.html')

def counter(request):
    return render(request,'counter.html')

def namePin(request):
    namePin=Data.objects.all()
    return render(request,'nameAndPin.html',{'namepin':namePin})

def delete(request, id):
    data=Data.objects.get(id=id)
    data.delete()
    return redirect('namePin')

def upload_images(request):
    if request.method=='POST':
        img = request.FILES.getlist('images')
        for image in img:
            MultipleImageUpload.objects.create(images=image)
    
    all_images = MultipleImageUpload.objects.all()
    return render(request, 'images.html', {'all_images':all_images})