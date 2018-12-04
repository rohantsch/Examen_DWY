from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings 
from django.conf.urls import url, include


urlpatterns = [
    path('', views.index, name="index"),
    path('registrar', views.registrar, name="registrar"),
<<<<<<< HEAD

    path('login',views.login,name="login"),
    path('accounts/profile/', views.cargar, name= "cargar"),
=======
    path('home', views.home, name="home"),
>>>>>>> master
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)