from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.

#creating tuple for status, whether post is draft or published
STATUS = ((0, "Draft"), (1, "Published"))
