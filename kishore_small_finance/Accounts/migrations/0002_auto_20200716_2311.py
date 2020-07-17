# Generated by Django 3.0.6 on 2020-07-16 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='loan_amount',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='account',
            name='outstanding_amount',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]