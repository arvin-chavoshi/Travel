from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Tag
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import CommentForm, NewsletterForm
from django.contrib import messages

# Create your views here.

POST_PER_PAGE = 4

def blog_home(request):
    posts = Post.objects.filter(is_published=True).order_by("-views")
    tags = Tag.objects.filter(is_featured=True)

    #------------ Search Posts --------------------------#
    search_query = request.GET.get("search")

    if search_query:
        posts = posts.filter(Q(title__icontains=search_query))

    #------------ Tags Filter -----------------------------#
    tag_query = request.GET.get("tag")
    if tag_query:
        posts = posts.filter(tags__name=tag_query)

    #------------ pagination posts -----------------------#
    pagination = Paginator(posts, POST_PER_PAGE)
    page_num = request.GET.get("page")
    page_obj = pagination.get_page(page_num)

    #------------ Newsletter validation ------------------#
    if request.method == "POST":
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            if request.POST.get("source") == "footer":
                messages.success(request, "Email Successfully Added.", extra_tags="footer")
            else :
                messages.success(request, "Email Successfully Added.", extra_tags="blog")

                

    else:
        form = NewsletterForm()

    context = {
        "posts" : posts,
        "page_obj" : page_obj,
        "tags" : tags,
        "form" : form,
    }

    return render(request, "blog/blog-home.html", context)

def blog_single(request):
    post = Post.objects.filter(is_published=True).first()
    if not post:
        return redirect("blog:blog-home")
    
    return redirect("blog:blog-post", pk=post.pk)

def blog_details(request, pk):
    post = get_object_or_404(Post, pk=pk)

    #------------Add View Amount with Click on View Post Button -----------------#
    post.views += 1
    post.save(update_fields=["views"])


    #------------ Comment Form Validation ------------------#
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            Comment.objects.create(
                post = post,
                name = form.cleaned_data["name"],
                email = form.cleaned_data["email"],
                subject = form.cleaned_data["subject"],
                message = form.cleaned_data["message"],
            )
            messages.success(request, "Comment added successfully.")
            return redirect("blog:blog-post", pk=post.pk)
            
    else :
        form = CommentForm()


    #-------------- Get Post Comments & Images ------------------#        
    comments = post.comments.all()
    post_images = post.images.all()

    #-------------- Get Post Next & Prev index ------------------#
    posts = Post.objects.filter(is_published=True).order_by("-views")
    next_post = None
    prev_post = None
    for i,x in enumerate(posts):
        if x.title == post.title:
            if i + 1 < len(posts):
                next_post = posts[i + 1]

            if i - 1 > 0:
                prev_post = posts[i - 1]

    #-------------- Blog-details Contexts -----------------------#
    context = {
        "post" : post,
        "comments" : comments,
        "post_images" : post_images,
        "next_post" : next_post,
        "prev_post" : prev_post,
    }

    return render(request, "blog/blog-single.html", context)