from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200)
    cover = models.TextField()
    body = models.TextField()
    published_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')  # User who published the post
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
