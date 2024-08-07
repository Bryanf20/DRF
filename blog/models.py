from django.db import models
from django.utils import timezone
from django.conf import settings

# Created models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    # allows us to filter published data only, rather than having to do it in the view
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_post')
    status = models.CharField(max_length=10, choices=options, default='published')
    objects = models.Manager() # Default manager 
    postobjects = PostObjects() # Custom manager

    # data return order
    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
