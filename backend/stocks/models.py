from django.db import models

# Create your models here.

class Stock(models.Model):
  symbol = models.CharField(max_length=255)
  open = models.FloatField()
  high = models.FloatField()
  low = models.FloatField()
  close = models.FloatField()
  volume = models.IntegerField()
  date = models.DateField()

  def __str__(self):
    return self.symbol + " : "+ str(self.date)