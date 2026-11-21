from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    image = models.ImageField(upload_to="posts/tag", blank=True, null=True)
    description = models.CharField(max_length=200, blank=True)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100,)
    image = models.ImageField(upload_to='posts/images')
    excerpt = models.TextField()
    content = models.TextField()
    quote = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    views = models.PositiveIntegerField(default=0)
    is_published = models.BooleanField(default=True)
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name="posts"
    )

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="comments",
    )
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name}  -  {self.subject}"

class PostImage(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name="images",
    )
    image = models.ImageField(upload_to="posts/gallery")

    def __str__(self):
        return f"image for - {self.post.title}  -  url = {self.image.url} "

class Newsletter(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
