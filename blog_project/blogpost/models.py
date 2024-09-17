from django.db import models
from django.utils import timezone                                                           
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=1000000)
    create_at = models.DateTimeField(default=timezone.now)