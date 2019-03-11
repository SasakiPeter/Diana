from django.db import models
from django.utils import timezone


class Day(models.Model):
    diary_title = models.CharField("dairy_title", max_length=200)
    diary_text = models.TextField("diary_text")
    pub_date = models.DateTimeField("pub_date", default=timezone.now)

    def __str__(self):
        return self.diary_title
