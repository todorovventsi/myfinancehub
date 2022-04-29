from django.views import generic as views


class TransactionsListView(views.ListView):
    template_name = 'budget_app/display_transactions_list.html'

