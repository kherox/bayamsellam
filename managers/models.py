from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _





# Create your models here.


class Manager(models.Model):
    user       = models.OneToOneField(User,on_delete=models.PROTECT) #,related_name='manager'
    contact    = models.CharField(max_length=45,verbose_name=_("Contact"))
    country    = models.CharField(max_length=45,verbose_name=_("Entrer votre Pays"))
    city       = models.CharField(max_length=45,verbose_name=_("Entrer votre ville"))
    created    = models.DateField(auto_now_add=True)

    def __str__(self) :
        return self.user.username 


