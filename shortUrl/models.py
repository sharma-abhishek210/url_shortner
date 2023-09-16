from django.db import models
from django.utils import timezone

class URL(models.Model):
    original_url = models.URLField(max_length=200)
    short_url = models.URLField(max_length=30, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    click_count = models.PositiveIntegerField(default=0)
    expiry_time = models.DateTimeField(default=timezone.now() + timezone.timedelta(days=7))

    def __str__(self):
        return f"Short URL for {self.original_url} is {self.short_url}"