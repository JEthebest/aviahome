from rest_framework.routers import DefaultRouter

from .views import (
    AirportViewSet,
    CityViewSet,
)

router = DefaultRouter()
router.register('airport',AirportViewSet,basename='airport')
router.register('city',CityViewSet,basename='city')

urlpatterns = router.urls