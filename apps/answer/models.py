from django.db import models

class Answers(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    question = models.CharField(max_length=255, blank=True, default='')
    answer = models.CharField(max_length=255, blank=True, default='')

    class Meta:
        ordering = ('created',)