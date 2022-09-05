from django.urls import path
from .views import register_account, register_card, register_customer, register_loan, register_receipt, register_third_party, register_wallet, register_transaction, register_notification, register_reward, register_currency


urlpatterns = [
    path("register/", register_customer, name ="registration"),   
    path("wallet/", register_wallet, name ="register"),   
    path("account/", register_account, name ="register_again"),   
    path("transaction/", register_transaction, name ="register_next"),   
    path("card/", register_card, name ="register_one"),   
    path("third_party/", register_third_party, name ="register_two"),   
    path("notification/", register_notification, name ="register_three"),   
    path("receipt/", register_receipt, name ="register_four"),   
    path("loan/", register_loan, name ="register_five"),   
    path("reward/", register_reward, name ="register_six"),   
    path("currency/", register_currency, name ="register_seven"),   
]