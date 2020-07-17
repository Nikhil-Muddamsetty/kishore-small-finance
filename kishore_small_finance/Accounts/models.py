from django.db import models
from Customers.models import Customer
from django.urls import reverse

# Create your models here.

class Account(models.Model):
    ACTIVE = 'A'
    INACTIVE = 'I'
    ACTIVENESS_CHOICE = [
    (ACTIVE, 'Active'),
    (INACTIVE, 'Inactive')
    ]
    loan_account_number = models.BigAutoField(primary_key=True)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE,db_index=True)
    loan_amount = models.FloatField(default=0)
    outstanding_amount = models.FloatField(null=True,blank=True,default=0)
    open_date = models.DateField(db_index=True)
    close_date = models.DateField(blank=True,null=True)
    current_Status = models.CharField(max_length=1,choices=ACTIVENESS_CHOICE,default=ACTIVE,db_index=True)

    def __str__(self):
        return str(self.customer.customer_name)

    def get_absolute_url(self):
        return reverse('account_home')
