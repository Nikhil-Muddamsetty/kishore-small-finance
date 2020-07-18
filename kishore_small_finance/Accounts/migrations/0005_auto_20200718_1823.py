# Generated by Django 3.0.6 on 2020-07-18 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0003_auto_20200716_0743'),
        ('Accounts', '0004_auto_20200718_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Customers.Customer'),
        ),
    ]
