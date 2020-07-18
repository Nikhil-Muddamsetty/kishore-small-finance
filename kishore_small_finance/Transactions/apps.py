from django.apps import AppConfig


class TransactionsConfig(AppConfig):
    name = 'Transactions'

    def ready(self):
         from .signals import create_initial_transaction
     
