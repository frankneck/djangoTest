from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.conf import settings


class ingredient(models.Model):
    title = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=1)

class Category(MPTTModel):
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=100)
    parent = TreeForeignKey(
        'self',
        related_name='children',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.title


class Step(models.Model):
    number_of_step = models.PositiveIntegerField(default=1)
    description = models.TextField()
    image_of_step = models.ImageField(upload_to='image_of_step/', blank=True)


class MPTTMeta:
    order_insertion_by = ['name']


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to="recipe_photos/", blank=True)
    complexity = models.CharField(max_length=100)
    anime_title = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category,
        related_name='recipe',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    cook_time = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

# TO DO class Direction(models.Model):


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
