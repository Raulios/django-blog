from django.contrib import admin
from core.models import Author

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name')
    search_fields = ('email', 'first_name', 'last_name')

admin.site.register(Author, AuthorAdmin)