from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True)
    body = models.TextField()
    image = models.ImageField(upload_to='blog_pics', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
