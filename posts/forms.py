from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from django import forms




class UserForm(UserCreationForm) :
    

    username       = forms.CharField(widget=forms.TextInput(attrs={"class" : 'form-control'}))
    password1      = forms.CharField(widget=forms.PasswordInput(attrs={"class" : 'form-control'}))
    password2      = forms.CharField(widget=forms.PasswordInput(attrs={"class" : 'form-control'}))
    first_name     = forms.CharField(widget=forms.TextInput(attrs={"class" : 'form-control'}))
    last_name      = forms.CharField(widget=forms.TextInput(attrs={"class" : 'form-control'}))
    email          = forms.EmailField(widget=forms.TextInput(attrs={"class" : 'form-control'}))
   
    username.label     = "Pseudo"
    password1.label    = "Mot de passe"
    password2.label    = "Confirmation"
    first_name.label   = "Nom"
    last_name.label    = "Prenom"
    email.label        = "Email"


    class Meta :
        model  = User 
        fields = ("username","password1","password2",'first_name', 'last_name', 'email')
       
    
 


class LoginForm(forms.Form) :
    username       = forms.CharField(widget=forms.TextInput(attrs={"class" : 'form-control'}))
    password1       = forms.CharField(widget=forms.PasswordInput(attrs={"class" : 'form-control'}))
    
    class Meta :
        model = User 
        #fields = ("username","password1")


    
