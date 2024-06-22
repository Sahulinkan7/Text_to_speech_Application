from django.urls import path
from .import views

urlpatterns = [
    path("",views.home_page,name="home"),
    path("get_mp3/",views.get_mp3,name="get_speech")
]
