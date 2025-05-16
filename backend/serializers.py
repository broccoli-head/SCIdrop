from rest_framework import serializers
from .models import Chest, Skin


class ChestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skin
        fields = ['id', 'name', 'price', 'rarity', 'cover']


class SkinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skin
        fields = ['id', 'name', 'price', 'rarity', 'cover',  'chestID']