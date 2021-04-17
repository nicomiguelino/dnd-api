from rest_framework.serializers import ModelSerializer, IntegerField
from .models import Character


class CharacterListSerializer(ModelSerializer):
    strength_modifier = IntegerField(read_only=True)
    dexterity_modifier = IntegerField(read_only=True)
    intelligence_modifier = IntegerField(read_only=True)
    constitution_modifier = IntegerField(read_only=True)
    wisdom_modifier = IntegerField(read_only=True)
    charisma_modifier = IntegerField(read_only=True)

    class Meta:
        model = Character
        fields = '__all__'
