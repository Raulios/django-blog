from django.db import models

from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True, null=True, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return u'{0}'.format(self.name)

    def __unicode__(self):
        return u'{0}'.format(self.name)

class Post(models.Model):

    title = models.CharField(max_length=250, blank=False, null=False, unique=True)
    summary = models.CharField(max_length=1000, blank=True, null=True)
    tags = models.CharField(max_length=250, blank=True, null=True)

    slug = models.SlugField(max_length=250, blank=True, null=True, unique=True)

    body = models.TextField()

    main_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    publish = models.BooleanField(default=False)

    category = models.ForeignKey(Category, blank=False, null=False, default=1)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Posts"

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return u'{0}'.format(self.title)

    def __unicode__(self):
        return u'{0}'.format(self.title)