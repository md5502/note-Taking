from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.db import models
from markdown import markdown


# Create your models here.
class Note(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length=128)
    body = models.TextField()
    rendered_html = models.TextField(editable=False, default="")
    slug = AutoSlugField(populate_from="title", unique_with=["created_at"])
    markdown_file = models.FileField(upload_to="markdown_files/", blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if self.markdown_file:
            self.markdown_file.seek(0)
            file_content = self.markdown_file.read().decode("utf-8")
            self.body = file_content
        if self.body:
            self.rendered_html = markdown(self.body)

        super().save(*args, **kwargs)
