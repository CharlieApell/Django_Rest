from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    CATEGORY_CHOICES = [
        (food, 'Food'),
        (drinks, 'Drinks'),
        (restaurants, 'Restaurants'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    category = models.CharField(choices=CATEGORY_CHOICES)
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
