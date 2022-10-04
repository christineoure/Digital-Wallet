from urllib.request import Request
from django.shortcuts import render
from django.shortcuts import redirect

from wallet.models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, Third_party, Transaction, Wallet

# from wallet.models import Wallet
from .forms import CardRegistration, CustomerRegistrationForm, NotificationRegistration, Third_partyRegistration, WalletRegistration, AccountRegistration, TransactionRegistration, Third_partyRegistration, ReceiptRegistration, LoanRegistration, RewardRegistration, CurrencyRegistration

# Create your views here.

def register_customer(request):

    if request.method == 'POST':
        form =  CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    
    else: 
        form = CustomerRegistrationForm()

    return render(request, "wallet/register_customer.html", {"form": form})


def list_customers(request):
    customers = Customer.objects.all()
    return render (request, 'wallet/list_customers.html', {'customers': customers})


def customer_profile(request, id):
    customer = Customer.objects.get(id=id)
    return render (request, 'wallet/customer_profile.html', {'customer': customer})
    

def edit_customer(request, id):
    customer = Customer.objects.get(id=id)
    if request.method == 'POST':
        form = CustomerRegistrationForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect("customer_profile", id=customer.id) 
    else:
        form = CustomerRegistrationForm(request.POST, instance=customer)
        return render(request,"wallet/edit_customer.html",{'form':form})



def register_wallet(request):
    form = WalletRegistration()
    return render(request, "wallet/register_wallet.html", {"form": form})

def register_account(request):
    form = AccountRegistration()
    return render(request, "wallet/register_account.html", {"form": form})

def register_transaction(request):
    form = TransactionRegistration()
    return render(request, "wallet/register_transaction.html", {"form": form})

def register_card(request):
    form = CardRegistration()
    return render(request, "wallet/register_card.html", {"form": form})

def register_third_party(request):
    form_third_party = Third_partyRegistration()
    return render(request,"wallet/register_third_party.html", {"form": form_third_party})

def register_notification(request):
    form = NotificationRegistration()
    return render(request, "wallet/register_notification.html", {"form": form})

def register_receipt(request):
    form = ReceiptRegistration()
    return render(request, "wallet/register_receipt.html", {"form": form})

def register_loan(request):
    form = LoanRegistration()
    return render(request, "wallet/register_loan.html", {"form": form})

def register_reward(request):
    form = RewardRegistration()
    return render(request, "wallet/register_reward.html", {"form": form})

def register_currency(request):
    form = CurrencyRegistration()
    return render(request, "wallet/register_currency.html", {"form": form})



def list_wallets(request):
    wallets = Wallet.objects.all()
    return render(request,"wallet/list_wallets.html",{'wallets':wallets})

def wallet_profile(request, id):
    wallet = Wallet.objects.get(id=id)
    return render(request,"wallet/profile.html",{'wallet':wallet})  

def edit_wallet(request, id):
    wallet = Wallet.objects.get(id=id)
    if request.method == 'POST':
        form = WalletRegistration(request.POST, instance=wallet) 
        if form.is_valid():
            form.save()
            return redirect("wallet_profile", id=wallet.id)
        else:
            form = WalletRegistration(request.POST, instance=wallet) 
            return render(request, 'wallet/edit_wallet.html', {'form': form})



def list_accounts(request):
    accounts = Account.objects.all()
    return render(request,"account/list_accounts.html",{'accounts':accounts})

def account_profile(request, id):
    account = Account.objects.get(id=id)
    return render(request,"account/profile.html",{'account':account})  

def edit_account(request, id):
    account = Account.objects.get(id=id)
    if request.method == 'POST':
        form = AccountRegistration(request.POST, instance=account) 
        if form.is_valid():
            form.save()
            return redirect("account_profile", id=account.id)
        else:
            form = AccountRegistration(request.POST, instance=account) 
            return render(request, 'account/edit_account.html', {'form': form})



def list_transactions(request):
    transactions = Transaction.objects.all()
    return render(request,"transaction/list_transactions.html",{'transactions':transactions})

def transaction_profile(request, id):
    transaction = Transaction.objects.get(id=id)
    return render(request,"transaction/profile.html",{'transaction':transaction})  

def edit_transaction(request, id):
    transaction = Transaction.objects.get(id=id)
    if request.method == 'POST':
        form = TransactionRegistration(request.POST, instance=transaction) 
        if form.is_valid():
            form.save()
            return redirect("transaction_profile", id=transaction.id)
        else:
            form = TransactionRegistration(request.POST, instance=transaction) 
            return render(request, 'transaction/edit_transaction.html', {'form': form})



def list_cards(request):
    cards = Card.objects.all()
    return render(request,"card/list_wcards.html",{'cards':cards})

def card_profile(request, id):
    card = Card.objects.get(id=id)
    return render(request,"cards/profile.html",{'card':card})  

def edit_card(request, id):
    card = Card.objects.get(id=id)
    if request.method == 'POST':
        form = CardRegistration(request.POST, instance=card) 
        if form.is_valid():
            form.save()
            return redirect("card_profile", id=card.id)
        else:
            form = CardRegistration(request.POST, instance=card) 
            return render(request, 'card/edit_card.html', {'form': form})



def list_third_partys(request):
    third_partys = Third_party.objects.all()
    return render(request,"third_party/list_third_party.html",{'third_partys':third_partys})

def third_party_profile(request, id):
    third_party = Third_party.objects.get(id=id)
    return render(request,"third_party/profile.html",{'third_party':third_party})  

def edit_third_party(request, id):
    third_party = Third_party.objects.get(id=id)
    if request.method == 'POST':
        form = Third_partyRegistration(request.POST, instance=third_party) 
        if form.is_valid():
            form.save()
            return redirect("third_party_profile", id=third_party.id)
        else:
            form = Third_partyRegistration(request.POST, instance=third_party) 
            return render(request, 'third_party/edit_third_party.html', {'form': form})



def list_notifications(request):
    notifications = Notification.objects.all()
    return render(request,"notification/list_notifications.html",{'notifications':notifications})

def notification_profile(request, id):
    notification = Notification.objects.get(id=id)
    return render(request,"notification/profile.html",{'notification':notification})  

def edit_notification(request, id):
    notification = Notification.objects.get(id=id)
    if request.method == 'POST':
        form = NotificationRegistration(request.POST, instance=notification) 
        if form.is_valid():
            form.save()
            return redirect("notification_profile", id=notification.id)
        else:
            form = NotificationRegistration(request.POST, instance=notification) 
            return render(request, 'notification/edit_notification.html', {'form': form})



def list_receipts(request):
    receipts = Receipt.objects.all()
    return render(request,"receipt/list_receipts.html",{'receipts':receipts})

def receipt_profile(request, id):
    account = Receipt.objects.get(id=id)
    return render(request,"receipt/profile.html",{'receipt':receipt})  

def edit_receipt(request, id):
    receipt = Receipt.objects.get(id=id)
    if request.method == 'POST':
        form = ReceiptRegistration(request.POST, instance=receipt) 
        if form.is_valid():
            form.save()
            return redirect("receipt_profile", id=receipt.id)
        else:
            form = ReceiptRegistration(request.POST, instance=receipt) 
            return render(request, 'receipt/edit_receipt.html', {'form': form})



def list_loans(request):
    loans = Loan.objects.all()
    return render(request,"loan/list_loans.html",{'loans':loans})

def loan_profile(request, id):
    loan = Loan.objects.get(id=id)
    return render(request,"loan/profile.html",{'loan':loan})  

def edit_loan(request, id):
    loan = Loan.objects.get(id=id)
    if request.method == 'POST':
        form = LoanRegistration(request.POST, instance=loan) 
        if form.is_valid():
            form.save()
            return redirect("loan_profile", id=loan.id)
        else:
            form = LoanRegistration(request.POST, instance=loan) 
            return render(request, 'loan/edit_loan.html', {'form': form})



def list_rewards(request):
    rewards = Reward.objects.all()
    return render(request,"reward/list_rewards.html",{'rewards':rewards})

def reward_profile(request, id):
    reward = Reward.objects.get(id=id)
    return render(request,"reward/profile.html",{'reward':reward})  

def edit_reward(request, id):
    reward = Reward.objects.get(id=id)
    if request.method == 'POST':
        form = RewardRegistration(request.POST, instance=reward) 
        if form.is_valid():
            form.save()
            return redirect("reward_profile", id=reward.id)
        else:
            form = RewardRegistration(request.POST, instance=reward) 
            return render(request, 'reward/edit_reward.html', {'form': form})



def list_currencys(request):
    currency = Currency.objects.all()
    return render(request,"currency/list_currencys.html",{'currencys':currencys})

def currency_profile(request, id):
    currency = Currency.objects.get(id=id)
    return render(request,"currency/profile.html",{'currency':currency})  

def edit_currency(request, id):
    currency = Currency.objects.get(id=id)
    if request.method == 'POST':
        form = CurrencyRegistration(request.POST, instance=currency) 
        if form.is_valid():
            form.save()
            return redirect("currency_profile", id=currency.id)
        else:
            form = CurrencyRegistration(request.POST, instance=currency) 
            return render(request, 'currency/edit_currency.html', {'form': form})