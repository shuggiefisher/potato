from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Post(models.Model):
    title = models.CharField(unique=True, null=False, blank=False, max_length=100)
    tweet = models.CharField(null=True, blank=True, max_length=140)
    body = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, to_field='username')
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, null=False, editable=False, max_length=100, db_index=True)
    
    def __unicode__(self):
        return str(str(self.author) + ' : ' + self.title)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post, to_field='title')
    comment = models.TextField(null=False, blank=False)
    author = models.ForeignKey(User, to_field='username')
    tweet = models.CharField(null=True, blank=True, max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return str(str(self.author) + ' : ' + self.comment)

admin.site.register(Post)
admin.site.register(Comment)