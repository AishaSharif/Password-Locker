class User:
    '''
    Class that lets user create a new account
    '''
    users = []

    def __init__(self, name, email, username,password):
        self.name = name
        self.email = email
        self.username = username
        self.phone_number = password

