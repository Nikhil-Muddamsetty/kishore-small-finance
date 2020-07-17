from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Transaction
from Accounts.models import Account
from django.views.generic import ListView

def uploadTransactionsView(request):
    if request.POST:
        transaction_data = request.POST.dict()
        transaction_date = transaction_data.pop('date')
        accounts_objects = Account.objects.all()
        for account in accounts_objects:
            loan_account_number_str = str(account.loan_account_number)
            if loan_account_number_str in transaction_data:
                amount = float(transaction_data.pop(loan_account_number_str))
                new_obj = Transaction(account=account,transaction_date=transaction_date,transaction_type='CR',transaction_amount=amount)
                account.outstanding_amount += amount
                if account.outstanding_amount >=0:
                    account.close_date = transaction_date
                    account.current_Status = 'I'
                account.save()
                new_obj.save()
        return redirect('/account/')

class TransactionAccountListView(ListView):
    model = Account
    template_name = "Transactions/transaction_update_list.html"
    fields = ['customer','loan_amount','outstanding_amount']

class TransactionDisplayByDateListView(ListView):
    model = Transaction
    template_name = 'Transaction/transaction_account_list.html'
