from django.db import models

# Create your models here.
class Product( models.Model ):
    dbid            = models.CharField( max_length= 100 )
    name            = models.CharField( max_length= 100 )
    value           = models.FloatField()
    discount_value  = models.FloatField()
    stock           = models.IntegerField()