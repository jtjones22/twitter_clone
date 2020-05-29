from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Profile(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)
    following = models.ManyToManyField(
        'self',
        symmetrical=False,
        blank=True,
        related_name='followings'
    )
