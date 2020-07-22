# Generated by Django 3.0.6 on 2020-07-22 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Transactions', '0005_transaction_transaction_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='transaction_type',
            field=models.CharField(choices=[('CR', 'Credit'), ('DR', 'Debit'), ('IP', 'Initial Payment To Customer')], default='CR', max_length=2),
        ),
    ]
