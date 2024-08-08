from rest_framework.routers import DefaultRouter
from api.views import UserModelViewSet, StockModelViewSet, ProductModelViewSet, BusinessModelViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('stocks', StockModelViewSet)
router.register('products', ProductModelViewSet)
router.register('business', BusinessModelViewSet)


urlpatterns = [

]

urlpatterns.extend(router.urls)
