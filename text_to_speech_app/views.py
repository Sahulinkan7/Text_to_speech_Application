from django.shortcuts import render
from .forms import TextForm
from django.http import JsonResponse
from django.contrib import messages
from Text_To_Speech_SRC.components.text_to_speech import TextToSpeechApplication
from Text_To_Speech_SRC.logger import logging
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.


def home_page(request):
    logging.info(f"You are in Home page .")
    form=TextForm()
    return render(request,"text_to_speech_app/home.html",{"form":form})


@csrf_exempt
def get_mp3(request):
    data=json.loads(request.body)
    print(data)
    text=data['text']
    tld=data['tld']
    print(text,tld)
    audio_string=TextToSpeechApplication().get_text_to_speech(text=text,accent=tld)
    result=audio_string.decode('utf8')
    newdata={
        'mp3string':result,
        'text':text,
        'tld':tld
    }
    print(newdata)
    return JsonResponse(json.dumps(newdata),content_type="application/json",safe=False)