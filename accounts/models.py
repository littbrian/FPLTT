from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    budget = models.DecimalField(max_digits=7, decimal_places=1, default=100.0)
    total_points = models.IntegerField(default=0)


    def __str__(self):
        return self.username 