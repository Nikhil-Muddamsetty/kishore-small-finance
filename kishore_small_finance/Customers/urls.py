from django.contrib import admin
from django.urls import path
from .views import CustomerCreateView,CustomerListView,CustomerUpdateView,CustomerDeleteView

urlpatterns = [
    path('create/' , CustomerCreateView.as_view() ),
    path('' , CustomerListView.as_view(), name='customer_home'),
    path('update/<pk>', CustomerUpdateView.as_view()),
    path('delete/<pk>', CustomerDeleteView.as_view()),
]
