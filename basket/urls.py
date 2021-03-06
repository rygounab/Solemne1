from django.urls import path
from basket import views


urlpatterns = [
    path('Opciones_Admin', views.OpcionesAdmin, name="OpcionesAdmin"),
    path('Opciones_coach', views.OpcionesCoach, name="OpcionesCoach"),
    path('list_player', views.listarJugador, name="listPlayer"),
    path('list_team', views.listarEquipo, name="listTeam"),
    path('ver_team', views.verEquipo, name="ver_team"),
    path('list_coach', views.listarEntreador, name="listCoach"),
    path('list_nomina', views.listarNominas, name="listnomina"),
    path('ver_nomina', views.verNominas, name="vernomina"),
    path('ver_juagdoresNomina/<int:id_Nomina>', views.verJugadoresNomina, name="ver_juagdoresNomina"),
    path('addPlayer', views.agregarJugador, name="addPlayer"),
    path('addTeam', views.agregarEquipo, name="addTeam"),
    path('addCoach', views.agregarEntrenador, name="addCoach"),
    path('addNomina', views.agregarNominas, name="addNomina"),
    path('editPlayer/<int:id_Jugador>', views.editarJugador, name="editPlayer"),
    path('editTeam/<int:id_Equipo>', views.editarEquipo, name="editTeam"),
    path('editCoach/<int:id_Entrenador>', views.editarEntrenador, name="editCoach"),
    path('deletePlayer/<int:id_Jugador>', views.eliminarJugador, name="deletePlayer"),
    path('deleteTeam/<int:id_Equipo>', views.eliminarEquipo, name="deleteTeam"),
    path('deleteCoach/<int:id_Entrenador>', views.eliminarEntrenador, name="deleteCoach"),
]
