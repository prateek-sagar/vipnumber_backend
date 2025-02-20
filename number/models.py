from django.db import models

class Number(models.Model):
    entry = models.CharField(max_length=10)
    price = models.IntegerField()
    discount = models.FloatField()

    def __str__(self):
        return self.entry
    
