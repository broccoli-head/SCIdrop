from django.db import models

class Chest(models.Model):
    name = models.CharField(max_length = 100)
    price = models.FloatField(default = 0)
    cover = models.ImageField(upload_to='media/chestCovers', blank = True, null = True)

class Skin(models.Model):
    chestID = models.ForeignKey(Chest, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    price = models.FloatField(default = 0)
    cover = models.ImageField(upload_to='media/skinCovers', blank = True, null = True)