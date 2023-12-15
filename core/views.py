from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .forms import ReceiptForm
from .models import Receipt


class SignupView(CreateView):
    """
    User Registration (signup) View
    """

    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class ReceiptListView(LoginRequiredMixin, ListView):
    model = Receipt
    context_object_name = "receipts"

    def get_queryset(self):
        """
        Return only receipts of the logged in user
        """
        return Receipt.objects.filter(user=self.request.user)


class ReceiptDetailView(LoginRequiredMixin, DetailView):
    model = Receipt
    context_object_name = "receipt"

    def get_object(self, queryset=None):
        """
        Make sure the user is the owner of the receipt
        """
        return get_object_or_404(
            Receipt, pk=self.kwargs.get("pk"), user=self.request.user
        )


class ReceiptCreateView(LoginRequiredMixin, CreateView):
    model = Receipt
    form_class = ReceiptForm
    success_url = reverse_lazy("receipt-list")

    def form_valid(self, form):
        """
        Assign the current User to the new Receipt
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReceiptUpdateView(LoginRequiredMixin, UpdateView):
    model = Receipt
    form_class = ReceiptForm
    success_url = reverse_lazy("receipt-list")


class ReceiptDeleteView(LoginRequiredMixin, DeleteView):
    model = Receipt
    success_url = reverse_lazy("receipt-list")
