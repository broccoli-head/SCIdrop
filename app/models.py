from django.db import models
import json

class Chest(models.Model):
    name = models.CharField(max_length = 100)
    content = models.JSONField()