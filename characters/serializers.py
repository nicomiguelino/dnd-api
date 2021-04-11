from drf_spectacular.utils import extend_schema_serializer, OpenApiExample
from rest_framework.serializers import ModelSerializer
from .models import Character


@extend_schema_serializer(
    examples=[
        OpenApiExample(
            'Valid Example #01',
            summary="Short summary",
            description="Sample description",
            value={
                'strength_score': 18,
                'dexterity_score': 17,
                'intelligence_score': 15,
                'constitution_score': 10,
                'wisdom_score': 8,
                'charisma_score': 7
            }
        )
    ]
)
class CharacterListSerializer(ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
