from django.shortcuts import render , redirect 
from django.http import HttpResponseRedirect , HttpResponse
from django.http import HttpResponse
from django.urls import reverse

from django.template import loader
from django.core.paginator import Paginator , EmptyPage ,PageNotAnInteger
from django.contrib.auth import login , authenticate 
from django.contrib.auth.models import User , Group
from django.views.decorators.http import require_http_methods

from django.core.exceptions import ObjectDoesNotExist
from django.contrib.postgres.search import SearchVector , SearchQuery , SearchRank


from .models import Post , Categorie 
from country.models import Countrie
from .forms import  UserForm 
from managers.forms import ManagerFrontendForm
from managers.models import Manager


# Create your views here.
@require_http_methods(["GET"])
def indexView(request) :
    # posts = Post.objects.order_by('-created')[:5]
    template  = 'posts/index.html'
    # categories = Categorie.objects.all()
    # country    = Countrie.objects.all()
    # context   = {"posts" : posts,"country" : country , "categories" : categories}
    return render(request,template,context=None)

@require_http_methods(["GET"])
def catalogueView(request) :
    posts_list      = Post.objects.all().order_by("-created")
    paginator  = Paginator(posts_list,10)
    page       = request.GET.get("page")
    posts      = paginator.get_page(page)
    template  = 'posts/catalogue.html'
    context   = {"posts" : posts}
    return render(request,template,context)

def searchView(request):
    vector = None
    query  = None 
    params = list(request.GET)
    is_categories  = False
    results  = None
    
    # for i in params :
    #     r      = request.GET.get(i)
    #     if  len(r) > 0:
    #         if query is None :
    #             query  = SearchQuery(r)
    #         else:
    #             query = query + SearchQuery(r)
    #         if vector is None :
    #             vector   =  SearchVector(i)
    #         else :
    #             vector = vector & SearchVector(i)

    name = None
    if request.GET.get('name') :
        name = request.GET.get('name')
    city = None
    if request.GET.get('city') :
        city = request.GET.get('city')
    categorie = None
    if request.GET.get('categorie') :
        if name is None and city is None :
            results =  Post.objects.filter(categorie=int((request.GET.get('categorie'))))
        if name is not None and city is not None :
            results =  Post.objects.filter(
                categorie=int((request.GET.get('categorie'))),
                city     = city ,
                name     = name
                )
        if name is not None and city is None :
            results =  Post.objects.filter(
                categorie=int((request.GET.get('categorie'))),
                name     = name
                )
        if name is None and city is not None :
            results =  Post.objects.filter(
                categorie=int((request.GET.get('categorie'))),
                city     = city
                )

    template  = 'posts/catalogue.html'
    if results != None  :
        paginator  = Paginator(results,10)
        page       = request.GET.get("page")
        posts      = paginator.get_page(page)
        context = {"posts" : posts}
        return render(request,template,context)
    else:
        return render(request,template,context=None)

     

@require_http_methods(["GET"])
def detailView(request,id,slug) :
    try:
        post = Post.objects.get(id=id,slug=slug)
        return render(request,"posts/details.html",{'post' : post})
    except ObjectDoesNotExist as e:
        print(e)
    

@require_http_methods(["GET"])
def contactView(request) :
    return render(request,"posts/contact.html",context=None)

@require_http_methods(["GET"])
def termsView(request) :
    return render(request,'posts/terms.html',context=None)

@require_http_methods(["GET"])
def registerView(request) :
    userform       = UserForm()
    managerform    = ManagerFrontendForm()
    return render(request,'posts/register.html',{'userform' : userform,"managerform":managerform})
    # if request.method == "POST" :
    #     user   = LoginForm(request.POST)
    #     if user.is_valid() :
    #         username  = user.cleaned_data.get("username")
    #         password  = user.cleaned_data.get("password1")
    #         new_user  = authenticate(username=username,password=password)
    #         login(request,new_user)
    #         return HttpResponseRedirect("/admin")
    # else :
@require_http_methods(["POST"])
def register(request) :
    
    if request.method == "POST" :
        userform     = UserForm(request.POST)
        managerform  = ManagerFrontendForm(request.POST)
        if userform.is_valid() and managerform.is_valid() :
            user , created  = User.objects.get_or_create(
                username    = userform.cleaned_data.get("username"),
                last_name   = userform.cleaned_data.get("last_name") ,
                first_name  = userform.cleaned_data.get("first_name") ,
                email       = userform.cleaned_data.get("email")
                 )
            password              = userform.cleaned_data.get("password1")
            if created :
                user.set_password(password)
                user.is_staff     = True
                #Update user after set password
                user.save()
                id = getattr(user,"id",None)
                #Save user profile
                managerform.cleaned_data["user"] = User.objects.get(id=id)
                manager  = Manager(
                    user     = managerform.cleaned_data.get("user"),
                    contact  = managerform.cleaned_data.get("contact"),
                    city     = managerform.cleaned_data.get("city"),
                    country  = managerform.cleaned_data.get("country")
                )
                manager.save(force_insert=False)
                if  manager == None:
                    user.delete()
                    return render(request,"posts/register.html",{'userform' : userform,"managerform":managerform})
                else :
                    #set user group
                    group    = Group.objects.get(name="Editeurs")
                    group.user_set.add(user)
                    group.save()
                    user                 = authenticate(username=user.username,password=password)
                    login(request,user)
                    manager = object()
                    user    = object()
                    return redirect("/")
        else :
            print(userform.errors)
            return render(request,"posts/register.html",{'userform' : userform,"managerform":managerform})
    else:
        return redirect("/createuser")

