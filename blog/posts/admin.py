from django.contrib import admin
from .models  import post
# Register your models here.

@admin.register(post)
class postAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_time']
    list_display_links = ['id', 'title']
    list_filter = ['date_time']
    search_fields = ['title', 'content']