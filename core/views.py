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


class ReceiptListView(ListView):
    model = Receipt
    context_object_name = "receipts"

    def get_queryset(self):
        """
        Return only receipts of the logged in user
        """
        return Receipt.objects.filter(user=self.request.user)


class ReceiptDetailView(DetailView):
    model = Receipt
    context_object_name = "receipt"


class ReceiptCreateView(CreateView):
    model = Receipt
    form_class = ReceiptForm
    success_url = reverse_lazy("receipt-list")

    def form_valid(self, form):
        """
        Assign the current User to the new Receipt
        """
        form.instance.user = self.request.user
        return super().form_valid(form)


class ReceiptUpdateView(UpdateView):
    model = Receipt
    form_class = ReceiptForm
    success_url = reverse_lazy("receipt-list")


class ReceiptDeleteView(DeleteView):
    model = Receipt
    success_url = reverse_lazy("receipt-list")
