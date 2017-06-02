from django.db import models

# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    office = models.CharField(max_length=100)
    age = models.SmallIntegerField()
    startdate = models.DateField()

    class Meta:
        ordering = ('name',)