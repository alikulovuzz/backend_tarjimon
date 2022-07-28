from django.db import models

class Translate(models.Model):
    text = models.CharField(max_length=5000)
    from_lang = models.CharField(max_length=10)
    to_lang = models.CharField(max_length=10)
    result = models.CharField(max_length=5000)
    izox = models.CharField(max_length=5000)