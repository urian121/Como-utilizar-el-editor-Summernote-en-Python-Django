from django.db import models
from django.utils import timezone


class Post(models.Model):
    autor = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    is_active = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f" {self.title} - {self.is_active} "

    class Meta:
        db_table = "tbl_posts"
        ordering = ['-created_at']
