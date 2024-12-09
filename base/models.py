from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.name)