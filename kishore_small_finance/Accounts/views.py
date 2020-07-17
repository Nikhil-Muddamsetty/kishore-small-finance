from django.shortcuts import render
from .models import Account
from django.views.generic import ListView,CreateView

class AccountListView(ListView):
    model = Account
    template_name = "Accounts/account_display_list.html"
    fields = ['loan_account_number','customer','loan_amount','outstanding_amount','open_date','close_date','current_Status']

class AccountCreateView(CreateView):
    model = Account
    template_name = "Accounts/account_create.html"
    fields = ['customer','loan_amount','open_date']
