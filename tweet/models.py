from django.db import models
from datetime import datetime
from django.conf import settings

# Create your models here.


class Tweet(models.Model):
    body = models.TextField(max_length=140)
    time = models.DateTimeField(
        default=datetime.now,
        blank=True
        )
    submitted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        )

    def __str__(self):
        return f'{self.submitted_by} | {self.body}'