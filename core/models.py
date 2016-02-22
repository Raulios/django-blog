from django.db import models

from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager

from django.utils.http import urlquote
from django.utils.text import slugify

import datetime
import pytz

# Create your models here.

class AuthorManager(BaseUserManager):

    def _create_user(self, email, password,
        is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = datetime.datetime.now(pytz.utc)
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email,
                is_staff=is_staff, is_active=True,
                is_superuser=is_superuser, last_login=now,
                date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,
                **extra_fields)

class Author(AbstractBaseUser, PermissionsMixin):
    '''
    The user who can write blogposts
    '''

    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField('first name', max_length=50, blank=False) # No delete
    last_name = models.CharField('last name', max_length=50, blank=False) # No delete



    def __str__(self):
        return u'{0}'.format(self.email)

    def __unicode__(self):
        return u'{0}'.format(self.email)

    is_staff = models.BooleanField('staff status', default=False,
    help_text='Designates whether the user can log into this admin '
                'site.')
    is_active = models.BooleanField('active', default=True,
    help_text='Designates whether this user should be treated as '
                'active. Unselect this instead of deleting accounts.')
    date_joined = models.DateTimeField('date joined', auto_now_add=True)

    objects = AuthorManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'

    def get_absolute_url(self):
        return "/author/%s/" % urlquote(self.email)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.email

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

class Tag(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, blank=True, null=True, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)

        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return u'{0}'.format(self.name)

    def __unicode__(self):
        return u'{0}'.format(self.name)

class Post(models.Model):

    title = models.CharField(max_length=250, blank=False, null=False, unique=True)
    summary = models.CharField(max_length=1000, blank=True, null=True)

    slug = models.SlugField(max_length=250, blank=True, null=True, unique=True)

    body = models.TextField(blank=False, null=False)

    main_image = models.ImageField(upload_to='blog_images/', blank=True, null=True)

    publish = models.BooleanField(default=False)

    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ('created_at',)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)

        self.summary = self.body[:150] + '...'

        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return u'{0}'.format(self.title)

    def __unicode__(self):
        return u'{0}'.format(self.title)