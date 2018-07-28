from django.urls import path

from . import views

urlpatterns = [
    # ex: /posts/
    path('', views.indexView, name='index'),
    path('catalogues',views.catalogueView,name="catalogue"),
    path('detail/<int:id>-<str:slug>/',views.detailView,name="detail"),
    path('contact',views.contactView,name="contact"),
    path('terms',views.termsView,name="terms"),
    path('createuser',views.registerView,name="createuser"),
    path('register',views.register,name="register"),
    path('search',views.searchView,name="search"),
   
]
#
    #path('detail/<int:id>-<str:slug>/',views.detailView,name="detail"),
