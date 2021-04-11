from rest_framework.generics import ListAPIView

from .models import Character
from .serializers import CharacterListSerializer


class CharacterListAPIView(ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterListSerializer
