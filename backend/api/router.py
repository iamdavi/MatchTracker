from django.urls.conf import include
from rest_framework.routers import DefaultRouter, SimpleRouter
from django.urls import path
from api.views import JugadorViewSet, UsuarioViewSet
from api import views

router = SimpleRouter()
# router.register(r"equipo", EquipoViewSet)
router.register(r"usuario", UsuarioViewSet)
router.register(r"jugador", JugadorViewSet)

urlpatterns = [
    path('equipo/', views.EquipoList.as_view()),
    path('equipo/<int:pk>/', views.EquipoDetail.as_view()),
    path('', include(router.urls)),
]
