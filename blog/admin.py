from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.

@admin.register(Post)

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
    #saying our content field is a summernote field, previously a django text field


#admin.site.register(Post)
