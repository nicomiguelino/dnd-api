from django.urls import path
from .views import CharacterListAPIView


app_name = 'characters'


urlpatterns = [
    path(
        '',
        CharacterListAPIView.as_view(),
        name='list'
    )
]
