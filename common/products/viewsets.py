from rest_framework import viewsets
from .models import Product
from .serializer import ProductSerializer

from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import action

def product_list(request):
    if( request.method == 'GET' ):
        return JsonResponse({'okas':'okas'})

class ProductViewSet( viewsets.ModelViewSet ):
    
    queryset            = Product.objects.all()
    serializer_class    = ProductSerializer

    @action(detail=True, methods=['post'])
    def set_products():
        return Response({'status': 'password set'})