from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib import messages

from aut.forms import  SingUpForm
from basket.models import  Coach

from django.contrib.auth import get_user_model

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

        print (password)

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
                    'Usuario o contraseña incorrectos! n a'
                )
        else:
            messages.error(
                request,
                'Usuario o contraseña incorrectos! none'
            )

    return render(request, template_name,data)

def logout_usuario(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def UsuarioCrear(request,id_Entrenador):
    template_name='entrenador/CrearUsuarioEntrenador.html'

    entrenador= Coach.objects.get(id=id_Entrenador)

    if request.method=='POST':
        form = SingUpForm(request.POST)
        if form.is_valid():
            # username=form.cleaned_data["username"]
            # password1=form.cleaned_data["password1"]
            # password2=form.cleaned_data["password2"]
            #
            #
            # userr=get_user_model().objects.create_user(username)
            # userr.password1=password1
            # userr.password2=password2
            #
            # userr.save()
            form.save()

            Coach.objects.filter(id=id_Entrenador).update(user=form.save())

            return HttpResponseRedirect(reverse('listCoach'))
    else:
        form=SingUpForm()

    return render(request,template_name,{'form':form})
