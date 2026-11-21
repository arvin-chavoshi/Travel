from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path("blog-home/", views.blog_home , name="blog-home"),
    path("blog-single/", views.blog_single , name="blog-single"),
    path("blog-single/<int:pk>/", views.blog_details, name="blog-post"),
]