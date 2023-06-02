from django.contrib import admin
from .models import Post, Comments
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Post)

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug':('title',)}
    summernote_fields = ('content')
    #saying our content field is a summernote field, previously a django text field


@admin.register(Comments)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')

#admin.site.register(Post)
