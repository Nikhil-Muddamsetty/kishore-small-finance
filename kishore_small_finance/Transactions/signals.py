from django.db.models.signals import post_save
from .models import Transaction
from django.dispatch import receiver
from Accounts.models import Account

@receiver(post_save,sender=Account)
def create_initial_transaction(sender,instance,created,**kwargs):
    print("signal recieved")
    if created:
        Transaction.objects.create(account=instance,transaction_date=instance.open_date,transaction_type='DR',transaction_amount=instance.loan_amount)
