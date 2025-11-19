from django.db import models

# Create your models here.


class Newsletter(models.Model):
    """ Model that sets the field for email subscription"""

    email = models.EmailField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.email
