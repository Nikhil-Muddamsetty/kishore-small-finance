from django.contrib import admin
from django.urls import path
from .views import AccountListView,AccountCreateView,AccountDeleteView,AccountDetailView

urlpatterns = [
    path('create/' , AccountCreateView.as_view() ),
    path('' , AccountListView.as_view(), name='account_home'),
    #path('update/<pk>', CustomerUpdateView.as_view()),
    path('delete/<pk>', AccountDeleteView.as_view()),
    path('details/<pk>', AccountDetailView.as_view()),
]
