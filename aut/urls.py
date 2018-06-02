from django.urls import path
from aut import views
from django.conf.urls import include


urlpatterns = [
    path('login', views.login_usuario, name="login"),
    path('logout', views.logout_usuario, name="logout"),
    path('SingIn/<int:id_Entrenador>', views.UsuarioCrear, name="SingIn"),
]
