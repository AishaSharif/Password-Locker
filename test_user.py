import unittest
from user import User


class test_user(unittest.TestCase):
    '''
    Test that defines test cases for the user class
    '''

    def setUp(self):
        '''
        Set up method to run before each test case
        '''
        self.new_user = User(
            'Nassim Taleb', 'nassim@blackswan.com', 'ntaleb', 'nasim123')

    def tearDown(self):
        '''
        Cleans up after each test has run
        '''
        User.users = []

    def test_init(self):
        '''
        Test if the object is initiated properly
        '''
        self.assertEqual(self.new_user.name, 'Nassim Taleb')
        self.assertEqual(self.new_user.email, 'nassim@blackswan.com')
        self.assertEqual(self.new_user.username, 'ntaleb')
        self.assertEqual(self.new_user.phone_number, 'nasim123')

    def test_save_user(self):
        '''
        Test if the user object is saved in the users list
        '''
        self.new_user.save_user()
        self.assertEqual(len(User.users), 1)


if __name__ == "__main__":
    unittest.main()
