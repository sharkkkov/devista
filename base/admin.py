from django.contrib import admin

from .models import Post, PostImage, Reference

class PostImageAdmin(admin.StackedInline):
    model = PostImage

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
       model = Post

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Reference)
class PostAdmin(admin.ModelAdmin):
    class Meta:
       model = Reference
