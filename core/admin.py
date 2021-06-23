from django.contrib import admin
from .models import Category, Post, Image, Comment


class ImageAdminInline(admin.StackedInline):
    model = Image
    extra = 1
    classes = ['collapse']


class CommentAdminInline(admin.StackedInline):
    model = Comment
    readonly_fields = ('date', 'up_vote', 'down_vote',)
    extra = 1
    classes = ['collapse']


class PostAdmin(admin.ModelAdmin):
    inlines = (ImageAdminInline, CommentAdminInline)
    readonly_fields = ('date',)
    fields = ('category', 'date', 'title', 'description',)
    list_display = ('title', 'category', 'date',)
    ordering = ('-date',)


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
