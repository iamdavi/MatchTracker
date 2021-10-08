from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()

router.register(r"equipos", views.EquipoViewSet, basename="equipo")