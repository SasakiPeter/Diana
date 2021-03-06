from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Diary(models.Model):
    title = models.CharField("title", max_length=200)
    text = models.TextField("text")
    pub_date = models.DateTimeField("pub_date", default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
