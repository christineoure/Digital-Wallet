from dataclasses import fields
from operator import mod
from rest_framework import serializers
from wallet.models import Account, Customer, Wallet, Card, Transaction, Loan, Receipt, Notification


# Create your models here.

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ("first_name", "age", "email", )

class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = ("customer", "date" , "user_name" ,  "pin" ,"isActive", "balance")

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("savings", "account_name", "account_type", "account_number",)

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ("card_name", "card_number",)

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ("transaction_profile", "account_name", "account_type", "account_number",)

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = ("account", "loan_type", "account_number", "account_type", "account_name", "guarantor", )

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = ("datetime", "time", "amount",)

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ( "message", "datetime", "statement", "receipt")

   