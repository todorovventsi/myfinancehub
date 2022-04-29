from django.urls import path

from mfh.budget_app.views import TransactionsListView

urlpatterns = [
    path('', TransactionsListView.as_view(), name='display transactions list')
]
