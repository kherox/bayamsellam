from ..models import Post

from django import template

register = template.Library()

@register.inclusion_tag("lastnews.html")
def default_lastnews() :
    posts    = Post.objects.all()[:2]
    return {"posts" : posts}