from django.contrib.auth.models import User
from django.db import models
from django.shortcuts import reverse


class Receipt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=255)
    date_of_purchase = models.DateField()
    item_list = models.TextField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def get_absolute_url(self):
        """
        Get URL for Detail View
        """
        return reverse("receipt-detail", kwargs={"pk": self.pk})

    def get_update_url(self):
        """
        Get URL for Update View
        """
        return reverse("receipt-update", kwargs={"pk": self.pk})

    def get_delete_url(self):
        """
        Get URL for Delete View
        """
        return reverse("receipt-delete", kwargs={"pk": self.pk})

    def __str__(self):
        return f"({self.pk}) - {self.store_name}"
