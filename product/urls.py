from rest_framework import routers
from .views import ProductViewSet, ManufacturerViewSet


router = routers.SimpleRouter()
router.register(r'products', ProductViewSet)
router.register(r'manufacturers', ManufacturerViewSet)

urlpatterns = router.urls
