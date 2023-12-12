from django.contrib.auth.models import User
from django.db import models


class Receipt(models.Model):
    """
    Receipt information
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255)
    date_of_purchase = models.DateField()
    item_list = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
