import random
import string
from dics import *

def gen_email(username):
    domain = random.choice(domains)
    email = f"{username}@{domain}"
    return email

def gen_username():
    username = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    return username

def gen_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.hexdigits, k=12))
    return password

def first_name():
    name = random.choice(first_names)
    return name

