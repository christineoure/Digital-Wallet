# from xml.parsers.expat import model
from xml.parsers.expat import model
from django import forms
from .models import Card, Customer, Notification,Third_party,Transaction, Wallet, Account, Receipt, Loan, Reward, Currency

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

class WalletRegistration(forms.ModelForm):
    class Meta:
        model = Wallet
        fields = "__all__"

class AccountRegistration(forms.ModelForm):
    class Meta:
        model = Account
        fields = "__all__"

class TransactionRegistration(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = "__all__"

class CardRegistration(forms.ModelForm):
    class Meta:
        model = Card
        fields = "__all__"

class Third_partyRegistration(forms.ModelForm):
    class Meta:
        model = Third_party
        fields = "__all__"

class NotificationRegistration(forms.ModelForm):
    class Meta:
        model = Notification
        fields = "__all__"

class ReceiptRegistration(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = "__all__"

class LoanRegistration(forms.ModelForm):
    class Meta:
        model = Loan
        fields = "__all__"

class RewardRegistration(forms.ModelForm):
    class Meta:
        model = Reward
        fields = "__all__"

class CurrencyRegistration(forms.ModelForm):
    class Meta:
        model = Currency
        fields = "__all__"