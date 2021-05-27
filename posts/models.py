from django.db import models
from users.models import User

# Create your models here.
class Post(models.Model):
    post = models.TextField()
    user_id = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField()
    user_id = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    post_id = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)