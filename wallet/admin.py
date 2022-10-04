
from django.contrib import admin
from.models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, Third_party, Transaction, Wallet

# Register your models here.



class CustomerAdmin(admin.ModelAdmin):
    list_display =("first_name", "last_name", "email", "age",)
    search_fields =("first_name", "last_name",)


admin.site.register(Customer,CustomerAdmin)

class WalletAdmin(admin.ModelAdmin):
    list_display = ("user_name", "customer", "balance",)
    search_fields = ("user_name", "customer",)


admin.site.register(Wallet, WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ("account_name", "account_type", "account_number",)
    search_fields = ("account_name", "account_type",)


admin.site.register(Account, AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ("amount", "transaction_type", "transaction_code", )
    search_fields = ("amount", "account_type",)


admin.site.register(Transaction, TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ("card_number", "card_status", "card_name",)
    search_fields = ("card_number", "card_status",)


admin.site.register(Card, CardAdmin)


class Third_partyAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "phone_number")
    search_fields = ("full_name", "email",)

    
admin.site.register(Third_party, Third_partyAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ("datetime", "statement", "receipt")
    search_fields = ("datetime", "statement",)


admin.site.register(Notification, NotificationAdmin)


class LoanAdmin(admin.ModelAdmin):
    list_display = ("account", "loan_type", "loan_term", "guarantor")
    search_fields = ("account", "loan_type",)


admin.site.register(Loan, LoanAdmin)


class ReceiptAdmin(admin.ModelAdmin):
    list_display = ("datetime", "file", "amount")
    search_fields = ("datetime", "file",)


admin.site.register(Receipt, ReceiptAdmin)

class RewardAdmin(admin.ModelAdmin):
    list_display = ("wallet", "points", "transaction")
    search_fields = ("wallet", "transaction",)


admin.site.register(Reward, RewardAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("country", "name", "symbol")
    search_fields = ("country", "name",)
admin.site.register(Currency, CurrencyAdmin)

