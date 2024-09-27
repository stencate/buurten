from django.db import models

# Create your models here.
# myapp/models.py
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    country = models.CharField(verbose_name="country", max_length=255, default="nl")
    # status = models.ForeignKey(MembershipStatus, on_delete=models.SET_NULL, null=True, default=1)
