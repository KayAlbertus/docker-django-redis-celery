from django.db import models

from django.db.models import Model
# Create your models here.
 
class exchange_modal(Model):
    current_price = models.TextField()
    last_refreshed = models.DateTimeField()


    class Meta:
        ordering = ['-id']
