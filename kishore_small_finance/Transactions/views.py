from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Transaction
from Accounts.models import Account
from django.views.generic import ListView

def uploadTransactionsView(request):
    if request.POST:
        transaction_data = request.POST.dict()
        transaction_date = transaction_data.pop('date')
        print("date: ",transaction_date)#----------------------------------------------------
        accounts_objects = Account.objects.all()
        for account in accounts_objects:
            loan_account_number_str = str(account.loan_account_number)
            if loan_account_number_str in transaction_data:
                print("match of account number found")#----------------------------------------------------
                amount = float(transaction_data.pop(loan_account_number_str))
                print("recieved amount =", amount)#----------------------------------------------------
                account.outstanding_amount += amount
                print("outstanding amount is :",account.outstanding_amount)#----------------------------------------------------
                if account.outstanding_amount >=0:
                    account.close_date = transaction_date
                    account.current_Status = 'I'
                account.save(force_update=True)
                Transaction.objects.create(account=account,transaction_date=transaction_date,transaction_type='CR',transaction_amount=amount,outstanding_amount_record=account.outstanding_amount)
        return redirect('/account/')

class TransactionAccountListView(ListView):
    model = Account
    template_name = "Transactions/transaction_update_list.html"
    fields = ['customer','loan_amount','outstanding_amount']

class TransactionMainListView(ListView):
    model = Account
    template_name = 'Transactions/transaction_account_list.html'
    fields = ['customer','loan_amount','outstanding_amount','open_date','current_Status','close_date']

class AccountStatementListView(ListView):
    model = Transaction
    template_name = 'Transactions/acc_statement_list.html'

    def get_queryset(self):
        account_ref = Account.objects.get(pk=self.kwargs['primary_key'])
        object_list = self.model.objects.filter(account=account_ref)
        return object_list
