import sys


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
                 return True

         return False









