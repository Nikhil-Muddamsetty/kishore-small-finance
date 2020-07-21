from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,TemplateView
from Customers.models import Customer
from django.urls import reverse_lazy
from django.db import models
from django.http import HttpResponseRedirect
from django.contrib import messages

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
        success_url = reverse_lazy('status_delete')
        error_url = reverse_lazy('status_delete')
        try:
            self.object.delete()
            messages.success(request, "The Customer's details has been deleted from the records")
            return HttpResponseRedirect(success_url)
        except models.ProtectedError:
            messages.error(request, "The Customer's details cannot be deleted becuase this customer has accounts linked to his profile")
            return HttpResponseRedirect(error_url)

class CustomerDeleteStatusView(TemplateView):
    template_name = 'Customers/customer_status_delete.html'

class CustomerAllDetailsView(ListView):
    model = Customer
    template_name = 'Customers/customer_all_accounts.html'
    def get_queryset(self):
        obj = Customer.objects.get(pk=self.kwargs['primary_key'])
        object_list = obj.account_set.all()
        return object_list
