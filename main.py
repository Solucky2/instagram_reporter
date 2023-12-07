from Driver import *
from utils.accounts import *
from utils.accounts import *
from scenarios.reports import *



if __name__ == "__main__":
    input_report_username = input("Podaj nazwę użytkownika do zgłosznia: ")
    for account in range(accounts_scenarios):
        report_account(user_name=input_report_username,
                       account=account)
