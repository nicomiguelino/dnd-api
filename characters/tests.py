from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase


class CharacterAPITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.character_list_url = reverse('characters:list')

    def create_character(self, request):
        return self.client.post(
            self.character_list_url, request['body'], format='json'
        )

    def assert_character_list_size(self, expected_size):
        response = self.client.get(
            self.character_list_url, format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), expected_size)

    def assert_created_character(self, request, response):
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        for ability_score in request['body']:
            self.assertEqual(
                response.data[ability_score],
                request['body'][ability_score]
            )

    def test_create_character(self):
        request = {
            'body': {
                'strength_score': 18,
                'dexterity_score': 17,
                'intelligence_score': 15,
                'constitution_score': 10,
                'wisdom_score': 8,
                'charisma_score': 7
            }
        }

        self.assert_character_list_size(0)
        response = self.create_character(request)
        self.assert_created_character(request, response)
        self.assert_character_list_size(1)
