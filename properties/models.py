from django.utils import timezone
from django.db import models


class Properties(models.Model):
    title = models.CharField(max_length=3000)
    address = models.CharField(max_length=3000)
    price = models.CharField(max_length=100)
    image_url = models.CharField(max_length=200)
    area = models.CharField(max_length=100)
    no_of_rooms = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = 'properties'
