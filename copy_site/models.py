from django.db import models

# Create your models here.

class WebPage(models.Model):
    url = models.URLField(unique=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url
