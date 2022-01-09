from django.urls.conf import include
from rest_framework.routers import SimpleRouter
from django.urls import path
from api import views

router = SimpleRouter()
router.register(r"usuario", views.UsuarioViewSet)
router.register(r"equipos", views.EquipoViewSet, basename="Equipo")

urlpatterns = [
    path('equipo/', views.EquipoList.as_view()),

    path('jugadores/', views.JugadorList.as_view()),
    path('jugadores/<int:pk>/', views.JugadorDetail.as_view()),

    path('partidos/', views.PartidoList.as_view()),
    path('partidos/<int:pk>/', views.PartidoDetail.as_view()),

    path('jornadas/', views.JornadaList.as_view()),
    path('jornadas/<int:pk>/', views.JornadaDetail.as_view()),

    path('rivales/', views.RivalList.as_view()),
    path('rivales/<int:pk>/', views.RivalDetail.as_view()),

    path('', include(router.urls)),
]
