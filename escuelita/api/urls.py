from rest_framework import routers
from .views import JugadorViewSet,EquipoViewSet

router = routers.DefaultRouter()

router.register('jugadores',JugadorViewSet,'jugadores')
router.register('equipos',EquipoViewSet,'equipos')

urlpatterns = router.urls