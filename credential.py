import sys
import pyperclip

from user import User

class Credential:

    global user_list
    credential_list = []

    def __init__(self, account_name, account_password, account_email):

        self.account_name = account_name
        self.account_password = account_password
        self.account_email = account_email

    def save_credential(self):

        Credential.credential_list.append(self)

    @classmethod
    def credential_exist(cls, account_name, account_password):

        for credential in cls.credential_list:

            if (credential.account_name == account_name) and (credential.account_password == account_password):

                return True

        return False

    @classmethod
    def display_credentials(cls):

        return cls.credential_list

    @classmethod
    def copy_credential(cls, credential):

        credential_found = Credential.find_by_credentials(credential)

        pyperclip.copy(credential_found.account_password)


