import sys
from credential import Credential


class User:

    user_list = []  # empty user list

    def __init__(self, user_name, user_password):

        self.user_name = user_name
        self.user_password = user_password

    def save_user(self):

        User.user_list.append(self)

    @classmethod
    def user_exists(cls, user_name, user_password):

         for user in cls.user_list:
             if (user.user_name == user_name) and (user.user_password == user_password):
                 return Credential.credential_list

         return False

    # def delete_user(self):
    #
    #     User.delete_user(self)

    # @classmethod
    # def user_not_exist(cls, user_name, user_password):
    #
    #     for









