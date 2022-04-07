from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    """All the Posts of the timeline"""
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'
        ordering = ['-publish_date']


class Like(models.Model):
    """Keeps likes of the post"""
    liked_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_likes')

    def __str__(self):
        return self.post.title

    class Meta:
        db_table = 'like'


class Comment(models.Model):
    """Keeps comments of the post"""
    content = models.TextField()
    commented_by = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    published_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'comment'
