
from django import forms

from .models import Manager

from country.models import Countrie


COUNTRY_LIST  =[]
country_liste = Countrie.objects.values("nom_en_gb")
COUNTRY_LIST  = [(q['nom_en_gb'],q['nom_en_gb']) for q in country_liste]


class ManagerFrontendForm(forms.ModelForm) :
    user            = forms.CharField(widget=forms.HiddenInput(),required=False)
    contact         = forms.CharField(widget=forms.TextInput(attrs={"class" : 'form-control'}))
    country         = forms.ChoiceField(widget=forms.Select(attrs={"class" : 'form-control'}),choices=COUNTRY_LIST)
    city            = forms.CharField(widget=forms.TextInput(attrs={"class" : 'form-control'}))

    contact.label   = "Numero de telephone" 
    city.label      = "Ville" 
    country.label   = "Pays" 
    
    class Meta :
        model = Manager 
        fields = ("contact","country","city")
        error_messages = {
            "contact"  : {'message' : " Le contact doit etre defini"},
            "country"  : {'message' : " Le pays doit etre defini"},
            "city "    : {'message' : " La ville doit etre defini"},
        }


    
