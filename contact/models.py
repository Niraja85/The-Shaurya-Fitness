from django.db import models
from django.utils import timezone
from django.core.validators import EmailValidator


# Create your models here.
class Contact(models.Model):
    """Contact form submission model"""
    name = models.CharField(max_length=60, blank=False, null=False)
    email = models.EmailField(
        max_length=100,
        validators=[
            EmailValidator(message="Email is invalid", code="invalid_email")
        ],
    )
    message = models.TextField(max_length=1000, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    # A method to return the name of the contact form submission
    def __str__(self):
        """Return the name of the contact form submission"""
        return self.name
