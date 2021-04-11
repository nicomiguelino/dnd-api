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
