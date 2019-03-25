from django.db import models

# Create your models here.
class TrendTable(models.Model):
    slider_one    = models.IntegerField()
    slider_two    = models.IntegerField()
    slider_three  = models.IntegerField()
    slider_four   = models.IntegerField()
    slider_five   = models.IntegerField()
    lowest_value  = models.IntegerField()
    highest_value = models.IntegerField()
    mean_value    = models.FloatField()