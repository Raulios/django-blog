__author__ = 'raulmolinasanchez'
from django.forms import ModelForm
from core.models import Post, Category

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body', 'main_image', 'publish', 'categories', 'tags')

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name',)