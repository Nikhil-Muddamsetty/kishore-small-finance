# Generated by Django 3.0.6 on 2020-07-22 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0003_auto_20200716_0743'),
        ('Accounts', '0006_account_amount_credited_to_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Customers.Customer'),
        ),
    ]
