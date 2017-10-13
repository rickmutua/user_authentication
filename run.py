#!/usr/bin/env python3.6

from user import User

from credential import Credential

def create_user(user_name, user_password):

    new_user = User(user_name, user_password)

    return new_user

def save_user(user):

    user.save_user()

def create_credential(account_name, account_password, account_email)
