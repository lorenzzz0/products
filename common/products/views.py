from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Product
from .serializer import ProductSerializer
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal


def products_list( request ):
    if request.method == 'GET' :
        products = Product.objects.all()
        serializer = ProductSerializer( products, many=True )
        data = {
            "Products":serializer.data
        }
        return JsonResponse(data, safe = False )

def validProduct( item ):
    isValid             = True
    errors              = []
    product             = item['Product']
    nameLength          = len( product['name'] )
    productValue        = float(product['value']) if ( 'value' in product ) else 0
    productDiscount     = float(product['discount_value']) if ( 'discount_value' in product ) else 'x'
    productStock        = int(product['stock']) if ( 'stock' in product ) else -1

    

    if ( nameLength > 55) or (nameLength < 3):
        errors.append( "Invalid product name" )
        isValid = False

    if (  productValue < 0 ) or ( productValue > 99999.90):
        errors.append( "Invalid value" )
        isValid = False
        
    if ( productDiscount == 'x') or ( productDiscount > productValue ):
        print('xxxx')
        print( product['id'] )
        print( productDiscount )
        print( productValue )
        errors.append( "Invalid discount value" )
        isValid = False

    if ( productStock < 0 ):
        errors.append( "Invalid stock value" )
        isValid = False
    
    response = {
        "isValid":isValid,
        "errors":errors
    }
    return response

def checkList( data ):
    countInvalid        = 0
    productsReport  = []
    for product in data['products']:
        respose = validProduct( product )
        allValid = respose['isValid']
        if respose['isValid'] == False:
            countInvalid = countInvalid + 1
            productsReport.append(
                {
                    "product_id": product['Product']['id'],
                    "errors":respose['errors']
                }
            )
    if( countInvalid == 0 ):
        for product in data['products']:
            value = product['Product']
            print( value )
            value['dbid'] = value.pop('id')
            print( value )
            serializer = ProductSerializer( data = value )
            if serializer.is_valid():
                serializer.save()
            else:
                print("ssssssss")

        return {"status": "OK"}
    else:
        return productsReport

@csrf_exempt
def products_bulk_insert( request ):
    try:
        if request.method == 'POST':
            data = JSONParser().parse( request )
            print( data )
            print( len(data['products']) )
            if len( data['products'] ) < 1:
                return JsonResponse( {'status':'ERROR COUNT'}, safe = False, status=400 )
            else:
                response = checkList( data )
                return JsonResponse(response, safe = False, status=200 )

    except:
       return JsonResponse( {'status':'ERROR'}, safe = False, status=400 )
