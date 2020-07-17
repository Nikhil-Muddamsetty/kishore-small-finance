"""kishore_small_finance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from authentication.views import IndexClassView
from Customers import urls as Customer_urls
from Accounts import urls as Account_urls
from Transactions import urls as Transaction_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , IndexClassView.as_view()),
    path('customer/',include(Customer_urls)),
    path('account/',include(Account_urls)),
    path('transaction/',include(Transaction_urls)),
]
