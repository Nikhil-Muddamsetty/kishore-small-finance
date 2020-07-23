from django.db.models.signals import post_save
from .models import Transaction
from django.dispatch import receiver
from Accounts.models import Account

@receiver(post_save,sender=Account)
def create_initial_transaction(sender,instance,**kwargs):
    print("signal recieved in transaction signal file")
    #if created:
    if kwargs['created']:
        print("creating initial")
        instance.outstanding_amount = (instance.loan_amount * -1)
        instance.save()
        Transaction.objects.bulk_create([
            Transaction(account=instance,transaction_date=instance.open_date,transaction_type='DR',transaction_amount=instance.loan_amount,outstanding_amount_record=(instance.loan_amount * -1),transaction_note='Total loan amount sanctioned'),
            Transaction(account=instance,transaction_date=instance.open_date,transaction_type='IP',transaction_amount=instance.amount_credited_to_customer,transaction_note='Money recieved by the account holder'),
        ])
