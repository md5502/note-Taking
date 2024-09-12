import markdown
from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=128)
    body = models.TextField()
    rendered_html = models.TextField(editable=False, default="")
    slug = AutoSlugField(populate_from="title", unique_with=["created_at"])

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        self.rendered_html = markdown(self.body)
        super().save(*args, **kwargs)
