from django.db import models

rarityList = [
    ('common', 'Common'),
    ('rare', 'Rare'),
    ('epic', 'Epic'),
    ('legendary', 'Legendary'),
]

class Chest(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(default = 0, max_digits = 6, decimal_places = 2)
    rarity = models.CharField(max_length = 20, choices = rarityList)
    cover = models.ImageField(upload_to='chestCovers', blank = True, null = True)

class Skin(models.Model):
    chestID = models.ForeignKey(Chest, on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)
    price = models.DecimalField(default = 0, max_digits = 6, decimal_places = 2)
    rarity = models.CharField(max_length = 20, choices = rarityList)
    cover = models.ImageField(upload_to='skinCovers', blank = True, null = True)