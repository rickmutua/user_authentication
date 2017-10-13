#!/usr/bin/env python3.6

from user import User

from credential import Credential


def create_user(user_name, user_password):

    new_user = User(user_name, user_password)

    return new_user


def save_user(user):

    user.save_user()


def create_credential(account_name, account_password, account_email):

    new_credential = Credential(account_name, account_password, account_email)

    return new_credential


def save_credential(credential):

    credential.save_credential()


def find_credential(account_name):

    return Credential.find_by_account_name(account_name)


def check_existing_credentials(account_name):

    return Credential.credential_exist(account_name)


def display_credentials():

    return Credential.display_credentials()


def main():
    print("Hello, Welcome to your password locker, please login")
    user_name = input()

    print(f"Hello {user_name}. What would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new credential, dc - display credentials, fc -find a credential, ex -exit")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Credential")
            print("-"*10)

            print("Account Name . . . .")
            account_name = input()

            print("Account Password . . . .")
            account_password = input()

            print("Account Email . . . .")
            account_email = input()

            save_credential(create_credential(account_name, account_password, account_email))

            print('\n')

            print(f"New Credential {account_name} {account_password} {account_email}")
            