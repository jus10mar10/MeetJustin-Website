from django.contrib import admin
from .models import Post, Contact, ContentManager

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'is_published', 'date')
    list_filter = ('is_published', 'type', 'date')  # Filter by these fields
    search_fields = ('title', 'content',)  # Search by title and content
    list_editable = ('is_published',)
    list_per_page = 25  # Show 25 records per page

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date')
    list_filter = ('date',)
    search_fields = ('name', 'email', 'message',)
    list_per_page = 25


admin.site.register(Post, PostAdmin)
admin.site.register(Contact, ContactAdmin)

admin.site.register(ContentManager)
