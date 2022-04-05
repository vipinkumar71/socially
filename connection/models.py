from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Following(models.Model):
    """Keeping follow/following connection"""
    following_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followers")
    followed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followings")

    def __str__(self):
        return self.followed_by.username

    class Meta:
        db_table = 'following'
