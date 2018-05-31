from django.urls import path
from aut import views


urlpatterns = [
    path('login', views.login_usuario, name="login"),
    path('logout', views.logout_usuario, name="logout"),
]
