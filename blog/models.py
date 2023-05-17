from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

#creating tuple for status, whether post is draft or published
STATUS = ((0, "Draft"), (1, "Published"))

# referencing db model created as we create django model

#inherits from standard model
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    # author has one to many relationship, one author can write many articles
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")
    #automatically defaults to current date & time
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    #allow to be blank
    excerpt = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    #many to many relationship, many users can like many posts
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)

    class Meta:
        #order our posts on the created on field, - sign is descending order
        ordering = ['-created_on']

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


