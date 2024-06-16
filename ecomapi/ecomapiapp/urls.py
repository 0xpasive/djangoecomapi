from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('category', CategoryViewSet)
router.register('product', ProductViewSet)
router.register('cart', CartViewSet)
router.register('cartitem', CartItemViewSet)
router.register('order', OrderViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]