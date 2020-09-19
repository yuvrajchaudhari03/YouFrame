from django.shortcuts import render
from .models import Image
import json
from django.http import HttpResponse


def index(request):
    image = Image.objects.all()
    return render(request,'index.html',{'image':image})
    
def uploadImage(request):
    if request.method == 'POST':
        if request.is_ajax():
            pic = request.FILES['image_file']
            uploaded_image = Image(pic=pic)
            uploaded_image.save()
            print(uploaded_image.pic.url)
            response_data = { 
                'url': uploaded_image.pic.url,
            }
    return HttpResponse(json.dumps(response_data))
