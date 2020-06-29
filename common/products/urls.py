'''
from rest_framework import routers
from .viewsets import ProductViewSet
from django.conf.urls import url, include

router = routers.SimpleRouter()
router.register('products', ProductViewSet)
urlpatterns = router.urls
'''

from django.urls import path
from .views import products_list
from .views import products_bulk_insert

urlpatterns = [
    path( 'products/', products_list ), 
    path( 'products/bulk_insert/', products_bulk_insert ), 
]
