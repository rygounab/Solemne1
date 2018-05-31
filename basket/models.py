from django.db import models
from basket.defines import POSITION_PLAYER_CHOICES, Tipo_Usuarios

from django.contrib.auth.models import AbstractUser

import json

# class Usuario(AbstractUser):
#     tipo=models.CharField(max_length=2, choices= Tipo_Usuarios, default='CO')

class Team(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos')

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=120)
    nickname = models.CharField(max_length=120)
    birthday = models.DateField(null=True)
    age = models.PositiveIntegerField(null=True)
    rut = models.CharField(max_length=12)
    email = models.EmailField()
    height = models.PositiveIntegerField(help_text="Altura en cm",null=True)
    weight = models.PositiveIntegerField(help_text="Peso en gramos",null=True)
    picture = models.ImageField(upload_to='picture_players')
    position = models.CharField(max_length=60, choices=POSITION_PLAYER_CHOICES)
    team = models.ForeignKey(Team, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.name


class Coach(models.Model):
    name = models.CharField(max_length=120)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    nickname = models.CharField(max_length=120)
    rut = models.CharField(max_length=12)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Nomina(models.Model):
    nombrePartido = models.CharField(max_length=120)
    fecha = models.DateField()
    hora = models.TimeField()
    jugador= models.ForeignKey(Player, on_delete=models.CASCADE)

    def set_jugador(self, x):
        self.jugador=json.dumps(x)

    def get_jugador(self, x):
        return json.loads(self.player)


    def __str__(self):
        return self.nombrePartido
