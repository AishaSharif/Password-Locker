import string
from random import randint, choice


class Credentials:
    '''
    creates new instance of credentials
    '''
    credential_list = []

    def __init__(self, account_url, account_username, account_password):
        self.account_url = account_url
        self.account_username = account_username
        self.account_password = account_password

    def save_credentials(self):
        '''
        function to save credentials
        '''
        Credentials.credential_list.append(self)

    @classmethod
    def display_credentials(cls):
        '''
        Method that returns a list of credentials
        '''
        return cls.credential_list

    def delete_credentials(self):
        '''
        Delete a saved credential from the credentials list
        '''
        Credentials.credential_list.remove(self)

