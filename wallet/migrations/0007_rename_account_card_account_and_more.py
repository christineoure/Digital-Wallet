# Generated by Django 4.0.6 on 2022-08-25 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0006_rename_account_name_account_account_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='card',
            old_name='Account',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='Card_Name',
            new_name='card_name',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='Card_Number',
            new_name='card_number',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='Card_Status',
            new_name='card_status',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='CVV',
            new_name='cvv',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='Pin_Number',
            new_name='pin_number',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='Signature',
            new_name='signature',
        ),
        migrations.RenameField(
            model_name='third_party',
            old_name='Account',
            new_name='account',
        ),
        migrations.RenameField(
            model_name='third_party',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='third_party',
            old_name='Full_Name',
            new_name='full_name',
        ),
        migrations.RenameField(
            model_name='third_party',
            old_name='isActive',
            new_name='isactive',
        ),
        migrations.RenameField(
            model_name='third_party',
            old_name='Phone_Number',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='third_party',
            old_name='Transaction_Cost',
            new_name='transaction_Cost',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='destination_Account',
            new_name='destination_account',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='origin_Account',
            new_name='origin_account',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='transaction_Code',
            new_name='transaction_code',
        ),
        migrations.RenameField(
            model_name='transaction',
            old_name='transaction_Type',
            new_name='transaction_type',
        ),
    ]