from drf_spectacular.utils import extend_schema, OpenApiExample
from rest_framework.generics import ListCreateAPIView

from .models import Character
from .serializers import CharacterListSerializer


@extend_schema(
    tags=['Characters']
)
class CharacterListAPIView(ListCreateAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterListSerializer

    @extend_schema(
        operation_id='Get list of all characters',
        examples=[
            OpenApiExample(
                'Example 1',
                response_only=True,
                value=[{
                    "id": 1,
                    "strength_modifier": 4,
                    "dexterity_modifier": 3,
                    "intelligence_modifier": 2,
                    "constitution_modifier": 0,
                    "wisdom_modifier": -1,
                    "charisma_modifier": -2,
                    "strength_score": 18,
                    "dexterity_score": 17,
                    "intelligence_score": 15,
                    "constitution_score": 10,
                    "wisdom_score": 8,
                    "charisma_score": 7
                }]
            )
        ]
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id='Create a character',
        responses={
            201: CharacterListSerializer
        },
        examples=[
            OpenApiExample(
                'Example 1',
                request_only=True,
                value={
                    'strength_score': 18,
                    'dexterity_score': 17,
                    'intelligence_score': 15,
                    'constitution_score': 10,
                    'wisdom_score': 8,
                    'charisma_score': 7
                }
            ),
            OpenApiExample(
                'Example 2',
                response_only=True,
                value= {
                    "id": 1,
                    "strength_modifier": 4,
                    "dexterity_modifier": 3,
                    "intelligence_modifier": 2,
                    "constitution_modifier": 0,
                    "wisdom_modifier": -1,
                    "charisma_modifier": -2,
                    "strength_score": 18,
                    "dexterity_score": 17,
                    "intelligence_score": 15,
                    "constitution_score": 10,
                    "wisdom_score": 8,
                    "charisma_score": 7
                }
            )
        ]
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
