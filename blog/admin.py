from django.contrib import admin
from .models import Post, Tag, Comment, PostImage, Newsletter

# Register your models here.

models_list = [
    Post,
    Tag,
    Comment,
    PostImage,
    Newsletter,
]

def register_models(models):
    for i in models:
        admin.site.register(i)

register_models(models_list)