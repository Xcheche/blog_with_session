from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to='post_images/',default='default.jpg')
    last_updated = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title 
    
    class Meta:
        ordering = ['-last_updated']
        
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'