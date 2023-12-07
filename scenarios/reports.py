from Driver import Driver
from scenarios.scenarios import *
import os


def report_account(user_name: str, account: Credentials):
    log_in_page_elements = LoginPageElements()
    driver = Driver(os.getenv("PATH"), account.ip_adress)
    driver.log_in(
        log_in_page_elements.email_input, account.login,
        log_in_page_elements.password_input, account.password
    )
    driver.get_user_page(user_name)
    for scenario in range(account_page_scenarios):
        driver.search_and_click(scenario)
    driver.check_report_sending()
