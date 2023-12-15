from datetime import date

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

from core.models import Receipt


class Command(BaseCommand):
    help = "Generate User and Receipt fixtures"

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS("Generating fixtures..."))

        # Create 3 users
        users = []
        for i in range(1, 4):
            user = User.objects.create_user(
                username=f"user{i}", password=f"password{i}"
            )
            users.append(user)

        # Create 7 receipts
        for i in range(1, 8):
            Receipt.objects.create(
                user=users[i % 3],
                store_name=f"Store {i}",
                date_of_purchase=date.today(),
                item_list=f"Item {i}",
                total_amount=i * 10.0,
            )

        self.stdout.write(self.style.SUCCESS("Fixtures generated successfully!"))
