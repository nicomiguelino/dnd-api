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

    def assert_created_character(self, response, expected_data):
        actual_data = response.data

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        ability_types = [
            'strength', 'dexterity', 'intelligence', 'constitution',
            'wisdom', 'charisma'
        ]

        for ability_type in ability_types:
            self.assertEqual(
                actual_data[f'{ability_type}_score'],
                expected_data[f'{ability_type}_score']
            )

            self.assertEqual(
                actual_data[f'{ability_type}_modifier'],
                expected_data[f'{ability_type}_modifier']
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

        expected_data = {
            'strength_score': 18,
            'strength_modifier': 4,
            'dexterity_score': 17,
            'dexterity_modifier': 3,
            'intelligence_score': 15,
            'intelligence_modifier': 2,
            'constitution_score': 10,
            'constitution_modifier': 0,
            'wisdom_score': 8,
            'wisdom_modifier': -1,
            'charisma_score': 7,
            'charisma_modifier': -2
        }

        self.assert_character_list_size(0)
        response = self.create_character(request)
        self.assert_created_character(response, expected_data)
        self.assert_character_list_size(1)
