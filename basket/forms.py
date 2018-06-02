from django.forms import ModelForm
from basket.models import Player, Team, Coach, Nomina
from django import forms

from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.models import User

class PlayerForm(ModelForm):
    class Meta:
        model = Player

        fields = [
            'name',
            'nickname',
            'birthday',
            'age',
            'rut',
            'email',
            'height',
            'weight',
            'position',
            'team',
            'picture',
        ]
        labels={
            'name':'Nombre',
            'nickname':'Apodo',
            'birthday':'Cumpleaños',
            'age':'Edad',
            'rut':'Rut',
            'email':'Email',
            'height':'Altura',
            'weight':'Peso',
            'position':'Posicion',
            'team':'Equipo',
            'picture':'Foto',
        }

        widgets={
            'birthday':forms.DateInput(),
        }

class TeamForm(ModelForm):
    class Meta:
        model = Team

        fields =[
            'name',
            'description',
            'logo',
        ]
        labels={
            'name':'Nombre',
            'description':'Descripcion',
            'logo':'Logo',
        }


class CoachForm(ModelForm):
    class Meta:
        model = Coach

        fields = [
            'name',
            'age',
            'email',
            'nickname',
            'rut',
            'team',
        ]
        labels={
            'name':'Nombre',
            'age':'Edad',
            'email':'Email',
            'nickname':'Apodo',
            'rut':'Rut',
            'team':'Team',
        }


class NominaForm(ModelForm):
    class Meta:
        model = Nomina


        fields = [
            'nombrePartido',
            'fecha',
            'hora',
            # 'jugador',
        ]
        labels={
            'nombrePartido':'NombrePartido',
            'fecha':'Fecha',
            'hora':'Hora',
        }

    jugadores_Seleccione_minimo_5_maximo_12_Presionando_ctrl=forms.ModelMultipleChoiceField(Player.objects.all(),required=False)
