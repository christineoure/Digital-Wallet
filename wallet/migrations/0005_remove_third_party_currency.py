# Generated by Django 4.0.6 on 2022-08-25 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0004_remove_receipt_transaction_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='third_party',
            name='Currency',
        ),
    ]