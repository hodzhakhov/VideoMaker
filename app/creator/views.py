from django.shortcuts import render
from django.http import HttpResponse
from .utils import create_video
#from .models import Clip
import os

def index(request):
    message = str(request.GET.get('message', 'No message provided'))
    #clip = Clip(message=message)
    #clip.save()
    result = create_video(message)
    with open(result, 'rb') as video_file:
        response = HttpResponse(video_file.read(), content_type='video/mp4')
        response['Content-Disposition'] = f'attachment; filename="message.mp4"'
    
    os.remove(result)

    return response
    
