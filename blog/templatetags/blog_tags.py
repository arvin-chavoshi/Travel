from django import template 
from blog.models import Tag, Post
from django.db.models import Count

register = template.Library()

@register.inclusion_tag("website/partials/tags_sidebar.html")
def tags_count():
    tags = Tag.objects.annotate(post_count=Count("posts"))
    return {"tags" : tags}

@register.inclusion_tag("website/partials/popular_posts.html")
def popular_posts():
    posts = Post.objects.filter(is_published=True).order_by("-views","-id")[:3]
    return {"posts" : posts}

@register.inclusion_tag("website/partials/tag_clouds.html")
def tag_clouds():
    tags = Tag.objects.all()
    return {"tags" : tags}