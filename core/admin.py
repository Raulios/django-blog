from django.contrib import admin
from core.models import Author, Post, Category, Tag

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')

class PostAdmin(admin.ModelAdmin):
    '''

    '''

    list_display = ('id', 'title', 'created_at', 'updated_at')
    exclude = ('slug',)
    list_display_links = ('id',)
    search_fields = ('title', 'categories', 'tags', 'created_at', 'updated_at')

class CategoryAdmin(admin.ModelAdmin):
    '''

    '''

    list_display = ('id', 'name', 'slug')
    exclude = ('slug',)
    list_display_links = ('id',)
    search_fields = ('name',)

class TagAdmin(admin.ModelAdmin):
    '''

    '''

    list_display = ('id', 'name', 'slug')
    exclude = ('slug',)
    list_display_links = ('id',)
    search_fields = ('name',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)