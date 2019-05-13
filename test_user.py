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

    


if __name__ == "__main__":
    unittest.main()
