from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from core.models import Receipt


class ReceiptDetailViewTest(TestCase):
    def setUp(self):
        # Set up any necessary data for your tests
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )

        Receipt.objects.create(
            pk=2,
            user=self.user,
            store_name="Test New Store",
            date_of_purchase="2087-04-11",
            item_list="Item A, Item B",
            total_amount=197.50,
        )

    # Test List View
    def test_list_view_anonymous(self):
        url = reverse("receipt-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_list_view_user(self):
        url = reverse("receipt-list")
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # Test Detail View
    def test_detail_view_anonymous(self):
        url = reverse("receipt-detail", kwargs={"pk": 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_detail_view_user(self):
        url = reverse("receipt-detail", kwargs={"pk": 2})
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # Test Update View
    def test_update_view_anonymous(self):
        url = reverse("receipt-update", kwargs={"pk": 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_update_view_user(self):
        url = reverse("receipt-update", kwargs={"pk": 2})
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    # Test Delete View
    def test_delete_view_anonymous(self):
        url = reverse("receipt-delete", kwargs={"pk": 2})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_delete_view_user(self):
        url = reverse("receipt-delete", kwargs={"pk": 2})
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
