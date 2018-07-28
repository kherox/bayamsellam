from django.contrib import admin
from django.contrib.admin import ModelAdmin
from rest_framework import serializers

from django import forms
from django.shortcuts import render

# Register your models here.

from .models import Order  , Post, Categorie

class CategorieAdmin(admin.ModelAdmin) :
    list_display = ("name","slug","created")
    list_filter = ["created"]
    fields = ['name']
    
# class PostSerializer(serializers.Serializer) :
#     class Meta :
#         owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
""" Class Form to customer form """
class PostAdminForm(forms.ModelForm):
    video   = forms.CharField(required=False)
    class Meta :
        #fields = ["name","price","categorie","video","city","links","links1","links2","links3","links4"]
        fields = ["name","price","categorie","video","city","links"]
        model = Post 
        
        
        # widgets = {
        #    'video' : forms.
        # }


class FilterPostAdmin(admin.ModelAdmin) : 
    
    def get_queryset(self,request) :
        qs   = super().get_queryset(request)
        return qs.filter(owner_id=request.user.id)

    # def get_list_select_related(self,request) :
    #     qs    = super(FilterPostAdmin,self).get_queryset(request)
    #     return qs.filter(owner_id=request.user.id)
        
    

    #def ge  

class FilterOrderAdmin(admin.ModelAdmin) :
    def get_queryset(self,request) :
        qs   = super().get_queryset(request)
        return qs.filter(owner_id=request.user.id)

    def lookups(self,request,model):
        qs   = model.get_queryset(request)
        return qs

    def formfield_for_foreignkey(self,db_field,request,**kwargs) :
        # if db_field.name == "owner" :
        #     kwargs["queryset"] = Post.objects.filter(owner_id=owner_id=request.user.id)
        if db_field.name == "referer" :
            kwargs["queryset"] = Post.objects.filter(owner_id=request.user.id)
        return super().formfield_for_foreignkey(db_field,request,**kwargs)
    # def get_list_select_related(self,request) :
    #     qs    = super(FilterOrderAdmin,self).get_queryset(request)
    #     return qs.filter(owner_id=request.user.id)

    # def change_view(self,request, object_id, form_url='', extra_context=None):
    #     print(object_id)
    #     return super().change_view(request, object_id, form_url, extra_context=extra_context)

    # def add_view(self,request, form_url='', extra_context=None) :
    #     return super().add_view(request, form_url, extra_context=extra_context)
      
        


    
        

class OrderAdmin(FilterOrderAdmin):
    
   pass  
   

class PostAdmin(FilterPostAdmin) :
    
    form = PostAdminForm
    #fields = ["name","price","categorie","video","city","links","links1","links2","links3","links4"]
    list_display = ("name","slug","created","categorie")
    list_filter  = ["created","categorie"]
    actions      = ["create_orders"]
    
    



    def save_model(self, request, obj, form, change) :
        obj.owner_id = request.user.id
        super().save_model(request, obj, form, change)
    
    def create_orders(self,request,queryset) :
        return render(request,"admin/orders.html",context=None)
    create_orders.short_description = " Create orders"

#admin.site.register(Order,OrderAdmin) 
admin.site.register(Post,PostAdmin) 
admin.site.register(Categorie,CategorieAdmin)      




