from django.db import models
from django.utils.text import slugify

# Create your models here.
class HomeTitle(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.name
    
class Category(models.Model):
    objects = None
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    text = models.TextField()
    image = models.ImageField()
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        
    def __str__(self):
        return self.name
    
class Post_Dizayne(models.Model):
    name = models.CharField(max_length=255)
    info = models.TextField()
    type = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField()
    slug = models.SlugField(unique=True, blank=True)
    
    def __str__(self):
        return self.name
    
class My_Sills(models.Model):
    title = models.CharField(max_length=100)
    sila = models.IntegerField()
    
    def __str__(self):
        return self.title
    
class About_Me(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=255)
    text =  models.TextField()
    
    def __str__(self):
        return self.title
    
class Link_me(models.Model):
    title = models.CharField(max_length=255)
    link = models.URLField()
    
    def __str__(self):
        return self.title