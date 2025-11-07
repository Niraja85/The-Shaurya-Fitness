from django.db import models

# Create your models here.


class Faq(models.Model):
    """ A model to display question and answers on
    frequently asked questions"""
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    question = models.CharField(max_length=200)
    answer = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question
