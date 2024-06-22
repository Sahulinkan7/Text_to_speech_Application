from django.shortcuts import render
from .forms import TextForm
from django.contrib import messages
# Create your views here.
def home_page(request):
    if request.method=="POST":
        form=TextForm(request.POST)
        if form.is_valid():
            messages.success(request,"submitted")
    else:
        form=TextForm()
    return render(request,"text_to_speech_app/home.html",{"form":form})