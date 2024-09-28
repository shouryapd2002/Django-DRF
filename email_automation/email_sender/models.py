from django.db import models

class EmailStatus(models.Model):
    recipient = models.EmailField()
    status = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)