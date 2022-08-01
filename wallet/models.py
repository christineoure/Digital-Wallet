from datetime import date, datetime
from email.policy import default
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
    ID_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    profile_picture = models.ImageField(default=False)
    Signature = models.ImageField(default=False)
    Employment_status = models.BooleanField(default=False)
    Marital_status = models.CharField(max_length=10,blank=True,)

class Wallet(models.Model):
    customer = models.OneToOneField("Customer", on_delete=models.CASCADE)
    Date = models.DateField()
    user_name = models.CharField(max_length=15)
    Pin = models.SmallIntegerField()
    isActive = models.BooleanField()
    Balance =models.IntegerField()

class Account(models.Model):
    Account_Type = models.CharField(max_length=15)
    Account_Number = models.IntegerField()
    Account_Name = models.CharField(max_length=15)
    Savings = models.IntegerField()
    Wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, )

class Transaction(models.Model):
    datetime = models.DateTimeField(default= datetime.now)
    Amount = models.IntegerField()
    Transaction_Type = models.CharField(max_length=15)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Third_Party = models.ForeignKey('Third_party', on_delete=models.CASCADE)
    Transaction_Code = models.CharField(max_length=15)
    Charge = models.IntegerField()
    Status = models.CharField(max_length=15)
    Origin_Account = models.ForeignKey("Account", on_delete=models.CASCADE,related_name="Transaction_Receipt")
    Destination_Account = models.ForeignKey("Account", on_delete=models.CASCADE)

class Card(models.Model):
    Card_Number = models.CharField(max_length=15)
    Card_Name = models.CharField(max_length=15)
    Account = models.ForeignKey("Account", on_delete=models.CASCADE) 
    Pin_Number = models.CharField(max_length=15, )
    CVV = models.PositiveSmallIntegerField()
    expiry_date = models.DateField() 
    Card_Status = models.CharField(max_length=15)
    Signature = models.ImageField(default=False)

class Third_party(models.Model):
    Full_Name = models.CharField(max_length=15)
    Email = models.CharField(max_length=15)
    Phone_Number = models.CharField(max_length=15)
    Transaction_Cost = models.CharField(max_length=15)
    Currency = models.OneToOneField("Third_party", on_delete=models.CASCADE)  
    isActive = models.BooleanField()    
    Account = models.ForeignKey("Account", on_delete=models.CASCADE)

class Notification(models.Model):
    message = models.TextField()
    datetime = models.DateField()
    Statement = models.CharField(max_length=15)
    Receipt = models.ForeignKey("Receipt", on_delete=models.CASCADE)

class Receipt(models.Model):
    Transaction = models.ForeignKey("Transaction", on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    File = models.FileField()
    Amount = models.PositiveIntegerField()

class Loan(models.Model): 
   Account = models.ForeignKey("Account", on_delete=models.CASCADE)
   Loan_Type = models.CharField(max_length=15,)
   Loan_Term = models.CharField(max_length=15, )
   Payment_Due_date = models.DateField()
   Guarantor = models.CharField(max_length=15, ) 
   Duration = models.DateField()
   Loan_Status = models.CharField(max_length=15, )
   Loan_borrow_date = models.DateField()
   Loan_Balance = models.IntegerField()   
   Wallet = models.ForeignKey("Wallet", on_delete=models.CASCADE) 

class Reward(models.Model):
    Date_Field = models.DateTimeField()
    Wallet = models.ForeignKey("Wallet", on_delete=models.CASCADE)
    Points = models.PositiveIntegerField()
    Transaction = models.ForeignKey("Transaction", on_delete=models.CASCADE)

class Currency(models.Model):
    Country =  models.CharField(max_length=15)
    Name = models.CharField(max_length=15)
    Symbol = models.CharField(max_length=5)
