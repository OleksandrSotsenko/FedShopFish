from django.db import models
from django.contrib.auth.models import User


COLORS = (
    ('BLK', 'black'),
    ('WHE', 'white'),
    ('GRY', 'grey'),
    ('BRW', 'brown'),
    ('RED', 'red'),
    ('GRN', 'green'),
    ('YLW', 'yellow'),
    ('BLE', 'blue',),
    ('PRP', 'purple'),
)


class Fish(models.Model):
    owner = models.ForeignKey(to=User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, blank=True)
    colors = models.CharField(max_length=3, choices=COLORS, default='GRY')
    life = models.IntegerField(blank=True)
    photo = models.ImageField(verbose_name='Photo', upload_to='fish/', blank=True)
    eating = models.CharField(max_length=150, blank=True)
    price = models.IntegerField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
      ordering = ('created_at',)

    def __str__(self):
        return f"{self.colors} {self.name}"
