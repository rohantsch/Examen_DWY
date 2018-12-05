from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings 
from django.conf.urls import url, include


urlpatterns = [
    path('', views.index, name="index"),
    path('registrar', views.registrar, name="registrar"),
    path('login',views.login,name="login"),
    path('home', views.home, name="home"),
    path('tienda', views.tienda, name="tienda"),
    path('tienda/crear', views.crear_tienda, name="crear_tienda"),
    path('accounts/profile/', views.cargar, name= "cargar"),

    path('usuario/crear', views.crear_usuario, name = "crear_usuario"),


    #MODULO LISTAS
    path('listas/crear', views.crear_lista, name="crear_lista"),
    path('listas/editar/<int:id>', views.editar_lista, name="editar_lista"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)