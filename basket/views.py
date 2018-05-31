from django.shortcuts import render
from basket.models import Player, Team, Coach, Nomina
from basket.forms import  PlayerForm, TeamForm, CoachForm, NominaForm
from django.shortcuts import redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.http import HttpResponseRedirect
from django.urls import reverse

#Protegemos las vistas con login_required
from django.contrib.auth.decorators import login_required

@login_required(login_url = '../aut/login')
def listarJugador(request):
    data = {}
    data['lista_objetos']=Player.objects.all()
    template_name='player/listarPlayer.html'
    return render(request, template_name,data)

def listarEquipo(request):
    data = {}
    data['lista_objetos']=Team.objects.all()
    template_name='equipo/listarEquipo.html'
    return render(request, template_name,data)

def listarEntreador(request):
    data = {}
    data['lista_objetos']=Coach.objects.all()
    template_name='entrenador/listarEntrenador.html'
    return render(request, template_name,data)

def listarNominas(request):
    data = {}
    data['lista_objetos']=Nomina.objects.all()
    template_name='entrenador/listarNominas.html'
    return render(request, template_name,data)

def agregarJugador(request):
    template_name='player/AgregarPlayer.html'
    if request.method=='POST':
        form=PlayerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # j=Player.objects.create()
            # j.name=form.data.get('name')
            # j.nickname=form.data.get('nickname')
            # j.birthday=form.data.get('birthday')
            # j.age=form.data.get('age')
            # j.rut=form.data.get('rut')
            # j.email=form.data.get('email')
            # j.height=form.data.get('height')
            # j.weight=form.data.get('weight')
            # j.position=form.data.get('position')
            # j.team=Team.objects.get(id=form.data.get('team'))
            # j.picture=form.data.get('image')
            # j.save()
            return HttpResponseRedirect(reverse('listPlayer'))
    else:
        form=PlayerForm()
    return render(request, template_name,{'form':form})

def agregarEquipo(request):
    template_name='equipo/AgregarEquipo.html'
    if request.method=='POST':
        form1=TeamForm(request.POST, request.FILES)
        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect(reverse('listTeam'))
    else:
        form1=TeamForm()
    return render(request, template_name,{'form1':form1})

def agregarEntrenador(request):
    template_name='entrenador/AgregarEntrenador.html'
    if request.method=='POST':
        form=CoachForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listCoach'))
    else:
        form=CoachForm()
    return render(request, template_name,{'form':form})

def editarJugador(request,id_Jugador):
    template_name='player/AgregarPlayer.html'
    jugador= Player.objects.get(id=id_Jugador)
    if request.method=='GET':
        form=PlayerForm(instance=jugador)
    else:
        form = PlayerForm(request.POST, request.FILES, instance=jugador)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listPlayer'))
    return render(request, template_name,{'form':form})

def editarEquipo(request,id_Equipo):
    template_name='equipo/AgregarEquipo.html'
    equipo= Team.objects.get(id=id_Equipo)
    if request.method=='GET':
        form1=TeamForm(instance=equipo)
    else:
        print("b")
        form1 = TeamForm(request.POST, request.FILES, instance=equipo)

        if form1.is_valid():
            form1.save()
            return HttpResponseRedirect(reverse('listTeam'))
    return render(request, template_name,{'form1':form1})

def editarEntrenador(request,id_Entrenador):
    template_name='entrenador/AgregarEntrenador.html'
    entrenador= Coach.objects.get(id=id_Entrenador)
    if request.method=='GET':
        form=CoachForm(instance=entrenador)
    else:
        form = CoachForm(request.POST, request.FILES, instance=entrenador)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('listCoach'))
    return render(request, template_name,{'form':form})

def eliminarJugador(request, id_Jugador):
    template_name='player/EliminarPlayer.html'
    jugador=Player.objects.get(id=id_Jugador)
    if request.method=='POST':
        jugador.delete()
        return HttpResponseRedirect(reverse('listPlayer'))
    return render(request, template_name,{'jugador':jugador})

def eliminarEquipo(request, id_Equipo):
    template_name='equipo/EliminarEquipo.html'
    equipo=Team.objects.get(id=id_Equipo)
    if request.method=='POST':
        equipo.delete()
        return HttpResponseRedirect(reverse('listTeam'))
    return render(request, template_name,{'equipo':equipo})

def eliminarEntrenador(request, id_Entrenador):
    template_name='entrenador/EliminarEntrenador.html'
    entrenador=Coach.objects.get(id=id_Entrenador)
    if request.method=='POST':
        entrenador.delete()
        return HttpResponseRedirect(reverse('listCoach'))
    return render(request, template_name,{'entrenador':entrenador})


def OpcionesAdmin(request):
    data = {}
    template_name='admin/opciones.html'
    return render(request, template_name,data)

def OpcionesCoach(request):
    data = {}
    template_name='entrenador/opciones.html'
    return render(request, template_name,data)



def add(request):
    data = {}
    if request.method == "POST":
        data['form'] = PlayerForm(request.POST, request.FILES)

        if data['form'].is_valid():
            # aca el formulario valido
            data['form'].save()

            return redirect('player_list')

    else:
        data['form'] = PlayerForm()

    template_name = 'player/add_player.html'
    return render(request, template_name, data)


def detail(request, player_id):

    data = {}
    template_name = 'player/detail_player.html'

    # SELECT * FROM player WHERE id = player_id
    data['player'] = Player.objects.get(pk=player_id)
    # import pdb;pdb.set_trace()

    return render(request, template_name, data)
