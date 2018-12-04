from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings 
from django.conf.urls import url, include
from django.conf import settings 



urlpatterns = [
    path('', views.index, name="index"),
    path('registrar', views.registrar, name="registrar"),
    path('home', views.home, name="home"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)