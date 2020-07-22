from django.shortcuts import render
from .models import Account
from django.views.generic import ListView,CreateView,DeleteView,DetailView
from .forms import AccountForm
from django.urls import reverse_lazy
from django.db import models
from django.contrib import messages
from django.http import HttpResponseRedirect

class AccountListView(ListView):
    model = Account
    template_name = "Accounts/account_home.html"
    fields = ['loan_account_number','customer','loan_amount','outstanding_amount','open_date','close_date','current_Status']

class AccountCreateView(CreateView):
    model = Account
    template_name = "Accounts/account_create.html"
    form_class = AccountForm

class AccountDeleteView(DeleteView):
    model = Account
    template_name = "Accounts/account_delete.html"

    def delete(self, request , *args , **kwargs):
        self.object = self.get_object()
        success_url = reverse_lazy('account_home')
        error_url = reverse_lazy('account_home')
        if(self.object.outstanding_amount>=0):
            self.object.delete()
            messages.success(request, "The Account's details has been deleted from the records")
            return HttpResponseRedirect(success_url)
        else:
            messages.error(request, "The Account's details cannot be deleted becuase the customer is yet to repay the loan")
            return HttpResponseRedirect(error_url)

class AccountDetailView(DetailView):
    model = Account
    template_name = "Accounts/account_details.html"
