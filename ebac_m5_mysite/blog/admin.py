from django.contrib import admin

# Register your models here.
from .models import Post
from .models import Project


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "status", "created_on")
    list_filter = ("status",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Project)
admin.site.register(Post, PostAdmin)


