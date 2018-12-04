from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings 
from django.conf.urls import url, include


urlpatterns = [
    path('', views.index, name="index"),
    path('registrar', views.registrar, name="registrar"),

    path('login',views.login,name="login"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)