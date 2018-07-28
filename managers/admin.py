from django.contrib import admin
from django import forms
from django.contrib.auth.models import User

# Register your models here.

from .models import Manager

class ManagerForm(forms.ModelForm) :

    class Meta :
        model   = Manager
        fields  = ("user","city","country","contact")

class ManagerInline(admin.StackedInline) :
    model = Manager
    can_delete = True
    verbose_name_plural = "Manager"
    extra = 0
    fk_name = "user"

class ManagerAdmin(admin.ModelAdmin) :
    #inlines      = (ManagerInline,)
    list_display = ("user","city","contact","country")
    #form         = ManagerForm

    def get_queryset(self,request) :
        qs = super().get_queryset(request)
        return qs.filter(user_id=request.user.id)

    def formfield_for_foreignkey(self,db_field,request,**kwargs) :
        # if db_field.name == "owner" :
        #     kwargs["queryset"] = Post.objects.filter(owner_id=owner_id=request.user.id)
        if db_field.name == "user" :
            kwargs["queryset"] = User.objects.filter(id=request.user.id)
        return super().formfield_for_foreignkey(db_field,request,**kwargs)

    # def save_model(self, request, obj, form, change):
    #     obj.user = User.objects.get(id=request.user.id)
    #     super().save_model(request, obj, form, change)

admin.site.register(Manager,ManagerAdmin)