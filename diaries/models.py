from django.db import models
from django.utils import timezone


class Diary(models.Model):
    title = models.CharField("title", max_length=200)
    text = models.TextField("text")
    pub_date = models.DateTimeField("pub_date", default=timezone.now)

    def __str__(self):
        return self.title
