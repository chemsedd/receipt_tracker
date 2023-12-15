"""
URL configuration for receipt_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # list all receipts
    path("receipts/", views.ReceiptListView.as_view(), name="receipt-list"),
    # create a receipt
    path("receipts/create", views.ReceiptCreateView.as_view(), name="receipt-create"),
    # get a receipt details
    path("receipts/<int:pk>", views.ReceiptDetailView.as_view(), name="receipt-detail"),
    # delete a receipt
    path(
        "receipts/<int:pk>/delete",
        views.ReceiptDeleteView.as_view(),
        name="receipt-delete",
    ),
    # update a receipt
    path(
        "receipts/<int:pk>/update",
        views.ReceiptUpdateView.as_view(),
        name="receipt-update",
    ),
]
