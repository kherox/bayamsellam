from ..models import Categorie
from country.models import Countrie

from django import template

register = template.Library()

@register.inclusion_tag("searchbar.html")
def default_searchbar() :
    categories = Categorie.objects.all()
    country    = Countrie.objects.all()
    return {"categories" : categories , "country" : country}