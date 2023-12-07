import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


class Credentials:
    def __init__(self, login: str, password: str, ip_adress: str):
        self.login = login
        self.password = password
        self.ip_adress = ip_adress

    def return_pass(self):
        return self.login, self.password
