from django.db import models
from Accounts.models import Account

class Transaction(models.Model):
    CREDIT = 'CR'
    DEBIT = 'DR'
    INITIAL_PAYMENT_TO_CUSTOMER = 'IP'
    TRANSACTION_TYPE = [
    (CREDIT,'Credit'),
    (DEBIT,'Debit'),
    (INITIAL_PAYMENT_TO_CUSTOMER,'Initial Payment To Customer')
    ]
    transaction_id = models.BigAutoField(primary_key=True)
    account = models.ForeignKey(Account,on_delete=models.CASCADE,db_index=True)
    transaction_note = models.CharField(max_length=50)
    transaction_date = models.DateField(db_index=True)
    transaction_type = models.CharField(max_length=2,choices=TRANSACTION_TYPE,default=CREDIT)
    transaction_amount = models.FloatField()
    outstanding_amount_record = models.FloatField(null=True)
