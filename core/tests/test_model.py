from django.contrib.auth.models import User
from django.test import TestCase

from core.models import Receipt


class ReceiptModelTest(TestCase):
    """
    Test Receipt model
    """

    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        # Create a receipt
        self.receipt = Receipt.objects.create(
            pk=1,
            user=self.user,
            store_name="Test Store",
            date_of_purchase="2023-01-01",
            item_list="Item 1, Item 2",
            total_amount=50.00,
        )

    # test the receipt was created correctly

    def test_receipt_user(self):
        self.assertEqual(str(self.receipt.user), "testuser")

    def test_receipt_store_name(self):
        self.assertEqual(str(self.receipt.store_name), "Test Store")

    def test_receipt_date_of_purchase(self):
        self.assertEqual(str(self.receipt.date_of_purchase), "2023-01-01")

    def test_receipt_item_list(self):
        self.assertEqual(str(self.receipt.item_list), "Item 1, Item 2")

    def test_receipt_total_amount(self):
        self.assertEqual(float(self.receipt.total_amount), 50.00)

    def test_receipt_absolute_url(self):
        self.assertEqual(self.receipt.get_absolute_url(), "/receipts/1")

    def test_receipt_update_url(self):
        self.assertEqual(self.receipt.get_update_url(), "/receipts/1/update")

    def test_receipt_delete_url(self):
        self.assertEqual(self.receipt.get_delete_url(), "/receipts/1/delete")
