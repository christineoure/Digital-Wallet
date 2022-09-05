from datetime import date, datetime
# from email.policy import default
# from email import message
# from email.policy import default
from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    gender = models.CharField(max_length=10)
    address = models.TextField()
    age = models.PositiveIntegerField(default=False)
    nationality = models.CharField(max_length=10)
    id_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    profile_picture = models.ImageField(default=False)
    signature = models.ImageField(default=False)
    employment_status = models.BooleanField(default=False)
    marital_status = models.CharField(max_length=10,blank=True,)

class Wallet(models.Model):
    customer = models.OneToOneField("Customer", on_delete=models.CASCADE)
    date = models.DateField()
    user_name = models.CharField(max_length=15)
    pin = models.SmallIntegerField()
    isActive = models.BooleanField()
    balance =models.IntegerField()

class Account(models.Model):
    account_type = models.CharField(max_length=15)
    account_number = models.IntegerField()
    account_name = models.CharField(max_length=15)
    savings = models.IntegerField()
    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, )

class Transaction(models.Model):
    datetime = models.DateTimeField(default= datetime.now)
    amount = models.IntegerField()
    transaction_type = models.CharField(max_length=15)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # Third_Party = models.ForeignKey('Third_party', on_delete=models.CASCADE)
    transaction_code = models.CharField(max_length=15)
    charge = models.IntegerField()
    status = models.CharField(max_length=15)
    origin_account = models.ForeignKey("Account", on_delete=models.CASCADE,related_name="Transaction_Receipt")
    destination_account = models.ForeignKey("Account", on_delete=models.CASCADE)

class Card(models.Model):
    card_number = models.CharField(max_length=15)
    card_name = models.CharField(max_length=15)
    account = models.ForeignKey("Account", on_delete=models.CASCADE) 
    pin_number = models.CharField(max_length=15, )
    cvv = models.PositiveSmallIntegerField()
    expiry_date = models.DateField() 
    card_status = models.CharField(max_length=15)
    signature = models.ImageField(default=False)

class Third_party(models.Model):
    full_name = models.CharField(max_length=15)
    email = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=15)
    transaction_Cost = models.CharField(max_length=15)
    # Currency = models.OneToOneField("Third_party", on_delete=models.CASCADE)  
    isactive = models.BooleanField()    
    account = models.ForeignKey("Account", on_delete=models.CASCADE)

class Notification(models.Model):
    message = models.TextField()
    datetime = models.DateField()
    statement = models.CharField(max_length=15)
    receipt = models.ForeignKey("Receipt", on_delete=models.CASCADE)

class Receipt(models.Model):
    # Transaction = models.ForeignKey("Transaction", on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    file = models.FileField()
    amount = models.PositiveIntegerField()

class Loan(models.Model): 
   account = models.ForeignKey("Account", on_delete=models.CASCADE)
   loan_type = models.CharField(max_length=15,)
   loan_term = models.CharField(max_length=15, )
   payment_due_date = models.DateField()
   guarantor = models.CharField(max_length=15, ) 
   duration = models.DateField()
   loan_status = models.CharField(max_length=15, )
   loan_borrow_date = models.DateField()
   loan_balance = models.IntegerField()   
   wallet = models.ForeignKey("Wallet", on_delete=models.CASCADE) 

class Reward(models.Model):
    date_field = models.DateTimeField()
    wallet = models.ForeignKey("Wallet", on_delete=models.CASCADE)
    points = models.PositiveIntegerField()
    transaction = models.ForeignKey("Transaction", on_delete=models.CASCADE)

class Currency(models.Model):
    country =  models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    symbol = models.CharField(max_length=5)
