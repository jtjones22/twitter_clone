from django.db import models
from django.conf import settings

from tweet.models import Tweet
# Create your models here.


class Notification(models.Model):
    reciever = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    read = models.BooleanField(
        default=False
    )
    tweet = models.ForeignKey(
        Tweet,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{str(self.tweet)}'