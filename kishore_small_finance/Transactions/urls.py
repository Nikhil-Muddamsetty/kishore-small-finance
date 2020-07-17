from django.contrib import admin
from django.urls import path
from .views import TransactionAccountListView,uploadTransactionsView

urlpatterns = [
    path('transact/submit/' , uploadTransactionsView),
    path('transact/' , TransactionAccountListView.as_view(), name='account_home'),
    #path('update/<pk>', CustomerUpdateView.as_view()),
    #path('delete/<pk>', CustomerDeleteView.as_view()),
]
