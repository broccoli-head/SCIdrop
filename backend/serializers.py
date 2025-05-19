from rest_framework import serializers
from .models import Chest, Skin, UserInventory


class ChestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chest
        fields = ['id', 'name', 'price', 'rarity', 'cover']


class SkinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skin
        fields = ['id', 'chestID', 'name', 'price', 'rarity', 'cover']


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInventory
        fields = ['balance', 'items']