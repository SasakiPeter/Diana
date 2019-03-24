from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Diary(models.Model):
    title = models.CharField("title", max_length=50)
    text = models.TextField("text")
    pub_date = models.DateTimeField("publish", default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def summary(self):
        return self.text[:50]

    def __str__(self):
        return self.title
