from user import User
from credentials import Credentials
from random import randint, choice
import string


def create_user(names, mail, user_name, pasword):
    '''
    Function to create a new user
    '''
    new_user = User(names, mail, user_name, pasword)
    return new_user


def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()


def create_credential(acc_url, acc_username, acc_pass):
    '''
    Function to create a new credential
    '''
    new_credential = Credentials(acc_url, acc_username, acc_pass)
    return new_credential


def save_credential(credit):
    '''
    Function to save credential
    '''
    credit.save_credentials()


def display_credential():
    '''
    Function to show a list of credentials
    '''
    return Credentials.display_credentials()


def delete_credential(credit):
    '''
    Function to delete credential
    '''
    credit.delete_credentials(credit)


def main():
    print('Hello! What is your name')
    username = input()
    print('\n')
    print(f'Hello {username}, What would you like to do?')
    print('\n')
    while True:
        print('Use these short codes: ca -> to create a password locker account, cc -> to create a new credential dc -> to display credentials, del -> to delete a credential , ex -> exit the contact list')
        print('\n')
        short_code = input().lower()

        if short_code == 'ca':
            print('Create a password locker account')
            print('*' * 20)

            print('Full Name')
            full_name = input()
            print('Email Address')
            e_address = input()
            print('Username')
            users_name = input()
            print('Password')
            passwrd = input()

            save_users(create_user(full_name, e_address, users_name, passwrd))

            print('\n')
            print(f'New user acount created. Your username is {users_name}')
            print('\n')

        elif short_code == 'cc':
            print('New Credentials')
            print('*' * 15)

            print('Name of the site')
            a_url = input()
            print('Your username for the site provided')
            a_username = input()

            print('Do you want a generated password or input your own. (g -> generate password, p -> input your own password)')
            p_ans = input()

            if p_ans == 'g':
                characters = string.ascii_letters + string.punctuation + string.digits
                a_pass = "".join(choice(characters)
                                 for x in range(randint(8, 12)))
                print('Your password is: {acc_pass}')
                print('\n')
            elif p_ans == 'p':
                print('Enter your password')
                a_pass = input()
            else:
                print('I did not get that. Please use the shortcodes provided')

            save_credential(create_credential(a_url, a_username, a_pass))
            print('New credentials for {a_url} created!')
            print('\n')

        elif short_code == 'dc':
            if display_credential():
                print('Here is a list of your saved passwords')
                print('\n')
                for credit in display_credential():
                    print(
                        f'url: {credit.account_url},  username: {credit.account_username},  password: {credit.account_password}')
                    print('\n')
            else:
                print('\n')
                print('You do not have any passwords saved')
                print('\n')

        elif short_code == 'del':
            pass

        elif short_code == 'ex':
            print('EXIT')
            break

        else:
            print('I didn\'t get that. Please use the short codes provided')


if __name__ == "__main__":
    main()
