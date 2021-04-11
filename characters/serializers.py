from rest_framework.serializers import ModelSerializer
from .models import Character


class CharacterListSerializer(ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
