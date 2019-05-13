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

    def save_user(self):
        '''
        Saves user object into the users list
        '''
        User.users.append(self)
