from django.db import models

# Create your models here.
class DataPoint(models.Model):
    node_name = models.CharField(max_length=250)
    datetime = models.DateTimeField(auto_now_add=True)
    data_type = models.CharField(max_length=250)
    data_value = models.FloatField()