from django.db import models

# Create your models here.
# Change these models to an ecommarce ones

class Made254(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()


    def __str__(self):
        return self.title

