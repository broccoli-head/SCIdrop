from django.db import models

class Chest(models.Model):
    name = models.CharField(max_length = 100)

class Skin(models.Model):
    chestID = models.ForeignKey(Chest, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    price = models.FloatField()