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
    def get(self, request, slug, *args, **kwargs):
        # now we need to get post object, a specific post object
        # to identify a specific post we can use the slug param, which is unique for each blog post
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('creted_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        #now we need to give this information to our render method
        return render(request, "post_detail.html", {
            "post": post,
            "comments": comments,
            "liked": liked
        },)

