from django.contrib import admin
from django.urls import path
from .views import CustomerCreateView,CustomerListView,CustomerUpdateView,CustomerDeleteView, CustomerAllDetailsView,CustomerDeleteStatusView

urlpatterns = [
    path('create/' , CustomerCreateView.as_view(), name='not_possible_foreignkey_exists'),
    path('' , CustomerListView.as_view(), name='customer_home'),
    path('update/<pk>', CustomerUpdateView.as_view()),
    path('delete/<pk>', CustomerDeleteView.as_view()),
    path('delete/status/', CustomerDeleteStatusView.as_view() ,  name='status_delete'),
    path('linkedAccounts/<int:primary_key>',  CustomerAllDetailsView.as_view()),
]
