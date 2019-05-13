import unittest
from credentials import Credentials


class TestCredentials(unittest.TestCase):
    '''
    class that defines test cases for the Credentials class
    '''

    def setUp(self):
        '''
        function to define instructions to be run before each test case
        '''
        self.new_credentials = Credentials(
            'http://twitter.com', 'nntaleb', 'ntaleb123')

    def tearDown(self):
        '''
        function that cleans up after each test has run
        '''
        Credentials.credential_list = []

    def test_init(self):
        '''
        test if the objects are initiated properly
        '''
        self.assertEqual(self.new_credentials.account_url,
                         'http://twitter.com')
        self.assertEqual(self.new_credentials.account_username, 'nntaleb')
        self.assertEqual(self.new_credentials.account_password, 'ntaleb123')

    def test_save_credentials(self):
        '''
        test if the credentials object is saved in the credentials_list
        '''
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_list), 1)

    def test_display_credentials(self):
        '''
        method to return a list of all the credentials saved
        '''
        self.assertEqual(Credentials.display_credentials(),
                         Credentials.credential_list)

   


if __name__ == "__main__":
    unittest.main()
