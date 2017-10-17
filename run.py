#!/usr/bin/env python3.6

from user import User

from credential import Credential


def user_exists(cls, user_name, user_password):
    for user in cls.user_list:
        if (user.user_name == user_name) and (user.user_password == user_password):
            return True
        return False

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
    print('\n')
    print("User Name . . . .")
    user_name = input()

    print('\n')
    print("User Password . . . .")
    user_password = input()

    print('\n')
    if user_name == user_name and user_password != user_password:
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

                print(f"New Credential {account_name} {account_password} {account_email} created")

                print('\n')

            elif short_code == 'dc':

                if display_credentials():

                    print("Here is a list of all your credentials")

                    print('\n')

                    for credential in display_credentials():

                        print(f"{credential.account_name} {credential.account_password} {credential.account_email}")

                        print('\n')

                else:
                    print('\n')

                    print("You dont seem to have any saved credentials")

                    print('\n')

            elif short_code == 'fc':

                print("Enter the account name you want to search for")

                search_account_name = input()

                if check_existing_credentials(search_account_name):

                    search_account_name = find_credential(search_account_name)

                    print(f"{search_account_name.account_name}")

                    print('-' * 20)

                    print(f"{search_account_name.account_password} {search_account_name.account_email}")

                else:
                     print("That credential doesn't exist")

            elif short_code == 'ex':
                print("GoodBye")

                break

            else:
                print("I didn't get that. Please use the short codes")


        # else:
        #      print("No such user account found.")



if __name__ == '__main__':

    main()
