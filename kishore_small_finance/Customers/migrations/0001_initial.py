# Generated by Django 3.0.6 on 2020-07-13 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(db_index=True, max_length=35)),
                ('customer_phone', models.IntegerField(blank=True, null=True)),
                ('customer_address', models.CharField(blank=True, max_length=60, null=True)),
            ],
        ),
    ]