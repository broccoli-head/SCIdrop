from rest_framework import serializers
from .models import Chest, Skin

class SkinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skin
        fields = ['id', 'name', 'price', 'rarity', 'cover']

class ChestSerializer(serializers.ModelSerializer):
    skins = serializers.SerializerMethodField()

    class Meta:
        model = Chest
        fields = ['id', 'name', 'price', 'rarity', 'cover', 'skins']

    def get_skins(self, id):
        skins = Skin.objects.filter(chestID = id)
        return SkinSerializer(skins, many = True, context = self.context).data
