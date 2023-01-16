from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    calories = models.FloatField()
    protein = models.FloatField()
    fat = models.FloatField()
    carbs = models.FloatField()
    quantity = models.FloatField()


class Recipe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    ingredients = models.ManyToManyField(Ingredient)
    serving_size = models.FloatField()
    prep_time = models.DurationField()

    def __str__(self):
        return self.name
