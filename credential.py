import sys
# import pyperclip
# import string
# import random

from user import User


class Credential:

    # global user_list
    # credential_list = []

    def __init__(self, account_name, account_password, account_email):

        self.account_name = account_name
        self.account_password = account_password
        self.account_email = account_email

    def save_credential(self):

        Credential.credential_list.append(self)

    def delete_credential(self):

        Credential.credential_list.remove(self)

    @classmethod
    def credential_exist(cls, account_name, account_password):

        for credential in cls.credential_list:

            if (credential.account_name == account_name) and (credential.account_password == account_password):

                return True

        return False

    @classmethod
    def display_credentials(cls):

        return cls.credential_list

    # @classmethod
    # def find_by_account_name(cls, account_name):
    #
    #     for credential in cls.credential_list:
    #         if credential.account_name == account_name:
    #             return credential
    #     return False

    # @classmethod
    # def copy_account_name(cls, account_name):
    #
    #     account_name_found = Credential.find_by_account_name(account_name)
    #     pyperclip.copy(account_name_found.account_name)
    #
    # @classmethod
    # def auto_generate_password(cls):
    #
    #     size = 8
    #     char = string.ascii_uppercase + string.ascii_lowercase + string.digits + '!@#$%^&*'
    #     return ''.join(random.choice(char) for _ in range(size))


