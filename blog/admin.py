from django.contrib import admin
from .models import Post
from django.utils.text import slugify

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "created_at", "status")
    list_filter = ("status", "created_at")
    search_fields = ("title", "content")
    ordering = ("-created_at",)