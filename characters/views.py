from drf_spectacular.utils import extend_schema
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
        operation_id='Get list of all characters'
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id='Create a character'
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
