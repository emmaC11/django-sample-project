from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
# Create your views here.

#vthis view here displays the post list
class PostList(generic.ListView):
    #using post as its model
    model = Post
    #using more built in methods
    #queryset which will contents of our post table, which then we are going to filter by status field, then order in descending order via created on date
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    #template name is the html file that our view will render
    template_name = 'index.html'
    paginate_by = 6

# this view is for viewing the post detail/content when clicked

class PostDetail(View):
    