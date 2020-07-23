from django import forms
from django.forms import ModelForm
from .models import Account

class DateInput(forms.DateInput):
    input_type = 'date'

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['customer','loan_amount','amount_credited_to_customer','open_date']
        widgets ={
        'open_date': DateInput()
        }
