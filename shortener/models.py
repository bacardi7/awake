from django.db import models

# Create your models here.

class PayPlan(models.Model):
    price = models.IntegerField()
    updated_at = models.DateTimeField(auto_now=True)
    create_at = models.DateTimeField(auto_now_add=True)