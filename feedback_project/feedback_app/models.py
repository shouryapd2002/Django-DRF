from django.db import models

# Create your models here.
class Feedback(models.Model):
    name= models.CharField(max_length=255)
    email= models.EmailField()
    Feedback= models.TextField()

    def __str__(self) -> str:
        return f"Feedback from {self.name}"