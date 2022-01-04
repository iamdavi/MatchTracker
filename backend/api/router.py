from django.urls.conf import include
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path
from api.views import  UsuarioViewSet, EquipoViewSet
from api import views

router = SimpleRouter()
router.register(r"usuario", UsuarioViewSet)
router.register(r"equipos", EquipoViewSet, basename="Equipo")

urlpatterns = [
    path('equipo/', views.EquipoList.as_view()),
    path('jugadores/', views.JugadorList.as_view()),
    path('jugadores/<int:pk>/', views.JugadorDetail.as_view()),
    path('', include(router.urls)),
]
