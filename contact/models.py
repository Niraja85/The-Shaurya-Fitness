from django.shortcuts import reverse
from django.db import models
from django.utils import timezone

# Create your models here.


class Contact(models.Model):
    """This model saves email in the DB"""
    name = models.CharField(max_length=60, blank=False, null=False)
    email = models.EmailField(max_length=254, blank=False, null=False)
    message = models.TextField
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

