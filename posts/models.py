from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from datetime import date


# Create your models here.

"""

 online :
        type : boolean
      name:
        type: string
      sub:
        type: string
      created:
        type: string
        format: date
      type : 
        type : string
"""

class Categorie(models.Model) :
    name                     = models.CharField(max_length=50)
    slug                     = models.SlugField(blank=True,editable=False)
    created                  = models.DateField()

    def __str__(self) :
        return  self.slug 
    class Meta:
      verbose_name = "Categorie"

class CategorieForm(ModelForm) :
        class Meta :
            model  = Categorie
            fields = ['name','created']

"""
 created:
        type: string
        format: date
      name:
        type: string
      content:
        type: string
      price:
        type: integer
      links:
        type: string
      owner:
        type: string
      category:
        type: string
      type : 
        type : string
        default : "Post"
      city : 
        type : string
"""
class Post(models.Model) :
    name          = models.CharField('Titre',max_length=150)
    slug          = models.SlugField(blank=True,editable=False)
    content       = models.TextField('Description')
    created       = models.DateField()
    price         = models.IntegerField('Le prix')
    owner         = models.ForeignKey(User,on_delete=models.CASCADE,editable=False) #serializers.HiddenField(default=serializers.CurrentUserDefault()) #
    city          = models.CharField(max_length=50)
    country       = models.CharField(max_length=100)
    categorie     = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    video         = models.CharField('Lien video',max_length=250,default=None)
    links         = models.ImageField("Image 1",max_length=250,upload_to='%Y/%m/%d/',)
    links1        = models.ImageField("Image 2 ",max_length=250,default=None,upload_to='%Y/%m/%d/')
    links2        = models.ImageField("Image 3 ",max_length=250,default=None,upload_to='%Y/%m/%d/')
    links3        = models.ImageField("Image 4",max_length=250,default=None,upload_to='%Y/%m/%d/')
    links4        = models.ImageField("Image  5 ",max_length=250,default=None,upload_to='%Y/%m/%d/')
    
    def __str__(self) :
          return self.name 
    class Meta:
      verbose_name = "Article"

class Order(models.Model):
    name                 = models.CharField(max_length=150) 
    owner                = models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    price                = models.IntegerField()
    categorie            = models.ForeignKey(Categorie,on_delete=models.CASCADE)
    referer              = models.ForeignKey(Post,on_delete=models.CASCADE)
    state                = models.BooleanField()
    provider             = models.CharField(max_length=50)
    duration             = models.IntegerField()
    begined              = models.DateTimeField('date de debut')

class OrderLine(models.Model) :
    viewnumber                 = models.IntegerField()
    clicknumber                = models.IntegerField()
    viewtime                   = models.TimeField()
    viewdate                   = models.DateField()
    viewierid                  = models.CharField(max_length=20)
    orderid                    = models.ForeignKey(Order,on_delete=models.CASCADE)



from django.db.models import signals
from django.template.defaultfilters import slugify


# function for use in pre_save
def post_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        slug = slugify(instance.name)  # change the attibute to the field that would be used as a slug
        new_slug = slug
        count = 0
        while Post.objects.filter(slug=new_slug).exclude(id=instance.id).count() > 0:
            count += 1
            new_slug = '{slug}-{count}'.format(slug=slug, count=count)

        instance.slug    = new_slug
        instance.created = date.today()
        #instance.owner_id   = User._get_pk_val(User)


# function for use in pre_save
def categorie_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        slug = slugify(instance.name)  # change the attibute to the field that would be used as a slug
        new_slug = slug
        count = 0
        while Categorie.objects.filter(slug=new_slug).exclude(id=instance.id).count() > 0:
            count += 1
            new_slug = '{slug}-{count}'.format(slug=slug, count=count)
        
        instance.slug    = new_slug
        instance.created = date.today()

# Execute signals pre_save
signals.pre_save.connect(post_pre_save, sender=Post)
signals.pre_save.connect(categorie_pre_save, sender=Categorie)
