from django.contrib import admin
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author)

    def __unicode__(self):
        return self.title


admin.site.register(Author)
admin.site.register(BlogPost)