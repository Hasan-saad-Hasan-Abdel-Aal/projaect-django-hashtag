from django.db import models

# Create your models here.

class Brand(models.Model):
    BrdName = models.CharField(max_length=40)

    def __str__(self):
        return self.BrdName