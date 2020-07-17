from django.db import models
from django.urls import reverse

# Create your models here.

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=35,db_index=True)
    customer_phone_number = models.IntegerField(blank=True,null=True)
    customer_address_line_1 = models.CharField(max_length=40,blank=True, null=True)
    customer_address_line_2 = models.CharField(max_length=40,blank=True, null=True)
    customer_address_city = models.CharField(max_length=40,blank=True, null=True)

    def __str__(self):
        return '%s %s ' % (self.customer_name, self.customer_address_city)
        #return self.customer_name

    def get_absolute_url(self):
        return reverse('customer_home')
