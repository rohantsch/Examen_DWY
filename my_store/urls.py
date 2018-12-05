from django.urls import path
from . import views
from django.conf.urls.static import static 
from django.conf import settings 
from django.conf.urls import url, include


urlpatterns = [
    path('', views.index, name="index"),
    
    path('login',views.login,name="login"),
    path('home', views.home, name="home"),
    path('accounts/profile/', views.cargar, name= "cargar"),
    
    path('usuario/crear', views.crear_usuario, name = "crear_usuario"),
    path('registrar', views.registrar, name="registrar"),
    path('cerrarsession',views.cerrar_session,name="cerrar_session"),

    #MODULO LISTAS
    path('listas/crear', views.crear_lista, name="crear_lista"),
    path('listas/editar/<int:id>', views.editar_lista, name="editar_lista"),

    #MODULO TIENDAS
    path('tienda', views.tienda, name="tienda"),
    path('tienda/crear', views.crear_tienda, name="crear_tienda"),
    path('tienda/editar/<int:id>', views.editar_tienda, name="editar_tienda"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)