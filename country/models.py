from django.db import models

# Create your models here.

class Countrie(models.Model) :
   code       = models.IntegerField()
   alpha2     = models.CharField(max_length=5)
   alpha3     = models.CharField(max_length=5)
   nom_en_gb  =  models.CharField(max_length=250) 
   nom_fr_fr  =  models.CharField(max_length=250)