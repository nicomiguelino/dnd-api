from django.db import models


class Character(models.Model):
    strength_score = models.PositiveSmallIntegerField()
    dexterity_score = models.PositiveSmallIntegerField()
    intelligence_score = models.PositiveSmallIntegerField()
    constitution_score = models.PositiveSmallIntegerField()
    wisdom_score = models.PositiveSmallIntegerField()
    charisma_score = models.PositiveSmallIntegerField()
