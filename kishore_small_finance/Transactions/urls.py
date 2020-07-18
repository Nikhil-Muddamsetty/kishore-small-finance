from django.contrib import admin
from django.urls import path
from .views import TransactionAccountListView,uploadTransactionsView,TransactionMainListView,AccountStatementListView

urlpatterns = [
    path('transact/submit/' , uploadTransactionsView),
    path('transact/' , TransactionAccountListView.as_view()),
    path('',TransactionMainListView.as_view(), name='transaction_home'),
    #path('update/<pk>', CustomerUpdateView.as_view()),
    #path('delete/<pk>', CustomerDeleteView.as_view()),
    path('accno/<int:primary_key>', AccountStatementListView.as_view()),
]
