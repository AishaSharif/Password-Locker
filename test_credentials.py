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

 
