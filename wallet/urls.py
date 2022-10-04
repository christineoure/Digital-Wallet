from django.urls import path
from .views import customer_profile, edit_loan, edit_wallet, list_customers, list_wallets, register_account, register_card, register_customer, register_loan, register_receipt, register_third_party, register_wallet, register_transaction, register_notification, register_reward, register_currency, edit_customer, wallet_profile, list_accounts, account_profile, edit_account, list_transactions, transaction_profile, edit_transaction, list_cards, card_profile, edit_card, list_third_partys, third_party_profile, edit_third_party, list_notifications, notification_profile, edit_notification, list_receipts, receipt_profile, edit_receipt, list_loans, loan_profile, list_rewards, reward_profile, edit_reward, list_currencys, currency_profile, edit_currency


urlpatterns = [
    path("register/", register_customer, name ="registration"),  
     path("list/", list_customers, name ="list_customers"),
    path("customers/<int:id>", customer_profile, name ="customer_profile"),
    path("customers/edit/<int:id>", edit_customer, name ="edit_customer"),


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

   

    path("list1/", list_wallets, name ="list_wallets"),
    path("wallet/<int:id>", wallet_profile, name ="wallet_profile"),
    path("wallet/edit/<int:id>", edit_wallet, name ="edit_wallet"),

    path("list2/", list_accounts, name ="list_accounts"),
    path("account/<int:id>", account_profile, name ="account_profile"),
    path("account/edit/<int:id>", edit_account, name ="edit_account"),

    path("list3/", list_transactions, name ="list_transactions"),
    path("transaction/<int:id>", transaction_profile, name ="transaction_profile"),
    path("transaction/edit/<int:id>", edit_transaction, name ="edit_transaction"),

    path("list4/", list_cards, name ="list_cards"),
    path("card/<int:id>", card_profile, name ="card_profile"),
    path("card/edit/<int:id>", edit_card, name ="edit_card"),

    path("list5/", list_third_partys, name ="list_third_partys"),
    path("third_party/<int:id>", third_party_profile, name ="third_party_profile"),
    path("third_party/edit/<int:id>", edit_third_party, name ="edit_third_party"),

    path("list6/", list_notifications, name ="list_notifications"),
    path("notification/<int:id>", notification_profile, name ="notification_profile"),
    path("notification/edit/<int:id>", edit_notification, name ="edit_notification"),

    path("list7/", list_receipts, name ="list_receipts"),
    path("receipt/<int:id>", receipt_profile, name ="receipt_profile"),
    path("receipt/edit/<int:id>", edit_receipt, name ="edit_receipt"),

    path("list8/", list_loans, name ="list_loans"),
    path("loan/<int:id>", loan_profile, name ="loan_profile"),
    path("loan/edit/<int:id>", edit_loan, name ="edit_loan"),

    path("list9/", list_rewards, name ="list_rewards"),
    path("reward/<int:id>", reward_profile, name ="reward_profile"),
    path("reward/edit/<int:id>", edit_reward, name ="edit_reward"),

    path("list10/", list_currencys, name ="list_currencys"),
    path("currency/<int:id>", currency_profile, name ="currency_profile"),
    path("currency/edit/<int:id>", edit_currency, name ="edit_currency"),
]