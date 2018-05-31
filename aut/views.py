from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def login_usuario(request):
    template_name='login.html'
    data={}

    logout(request)
    username=password=''
    if request.POST:
        username= request.POST['username']
        password= request.POST['password']
        user = authenticate(
            username=username,
            password=password
        )

        if user is not None:
            if user.is_active:
                if user.is_superuser:
                    login(request, user)
                    return HttpResponseRedirect(reverse('OpcionesAdmin'))
                if not user.is_superuser:
                    login(request, user)
                    return HttpResponseRedirect(reverse('OpcionesCoach'))
            else:
                messages.warning(
                    request,
                    'Usuario o contraseña incorrectos!'
                )
        else:
            messages.error(
                request,
                'Usuario o contraseña incorrectos!'
            )

    return render(request, template_name,data)

def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
