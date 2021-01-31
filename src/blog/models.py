from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    title = models.CharField(blank=False, max_length=100)
    content = models.TextField(blank=False)
    author = models.CharField(max_length=50)
    date = models.DateField(auto_now=False, auto_now_add=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"art_id": self.id})
