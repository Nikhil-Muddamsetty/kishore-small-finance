from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from Customers.models import Customer
from django.urls import reverse_lazy
from django.db import models
from django.http import HttpResponseRedirect

class CustomerCreateView(CreateView):
    model = Customer
    fields = ['customer_name','customer_phone_number','customer_address_line_1','customer_address_line_2','customer_address_city']
    template_name = 'Customers/customer_create.html'

class CustomerListView(ListView):
    model = Customer
    fields = ['customer_id','customer_name', 'customer_phone_number','customer_address_city']
    template_name = 'Customers/customer_home.html'

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = ['customer_name','customer_phone_number','customer_address_line_1','customer_address_line_2','customer_address_city']
    template_name = 'Customers/customer_update.html'

class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'Customers/customer_Delete.html'

    def delete(self, request , *args , **kwargs):
        self.object = self.get_object()
        success_url = reverse_lazy('customer_home')
        error_url = reverse_lazy('not_possible_foreignkey_exists')
        try:
            self.object.delete()
            return HttpResponseRedirect(success_url)
        except models.ProtectedError:
            return HttpResponseRedirect(error_url)
