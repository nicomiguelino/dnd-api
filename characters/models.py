from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


ability_score_validators = [
    MinValueValidator(1), MaxValueValidator(20)
]


class Character(models.Model):
    __common_args = dict(
        validators=ability_score_validators
    )

    strength_score = models.PositiveSmallIntegerField(**__common_args)
    dexterity_score = models.PositiveSmallIntegerField(**__common_args)
    intelligence_score = models.PositiveSmallIntegerField(**__common_args)
    constitution_score = models.PositiveSmallIntegerField(**__common_args)
    wisdom_score = models.PositiveSmallIntegerField(**__common_args)
    charisma_score = models.PositiveSmallIntegerField(**__common_args)

    def get_modifier(self, score):
        return (score - 10) // 2

    @property
    def strength_modifier(self):
        return self.get_modifier(self.strength_score)

    @property
    def dexterity_modifier(self):
        return self.get_modifier(self.dexterity_score)

    @property
    def intelligence_modifier(self):
        return self.get_modifier(self.intelligence_score)

    @property
    def constitution_modifier(self):
        return self.get_modifier(self.constitution_score)

    @property
    def wisdom_modifier(self):
        return self.get_modifier(self.wisdom_score)

    @property
    def charisma_modifier(self):
        return self.get_modifier(self.charisma_score)
