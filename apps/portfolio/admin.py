from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'is_published', 'date')
    list_filter = ('is_published', 'type', 'date')  # Filter by these fields
    search_fields = ('title', 'content',)  # Search by title and content
    list_editable = ('is_published',)
    list_per_page = 25  # Show 25 records per page

admin.site.register(Post, PostAdmin)