from django.db import models
from django.urls import reverse


class Lesson(models.Model):
    title = models.CharField(blank=False, max_length=100)
    teacher = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse("lessons:lesson-detail", kwargs={"pk": self.pk})
