from django.contrib import admin

from backend.models import Post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    '''

    '''

    list_display = ('id', 'title', 'category', 'tags', 'created_at', 'updated_at')
    exclude = ('slug',)
    list_display_links = ('id',)
    search_fields = ('title', 'category', 'tags', 'created_at', 'updated_at')

class BlogCategoryAdmin(admin.ModelAdmin):
    '''

    '''

    list_display = ('id', 'name', 'slug')
    exclude = ('slug',)
    list_display_links = ('id',)
    search_fields = ('name',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, BlogCategoryAdmin)