import unittest # importing the unittest module

from user import User # importing the user class

class TestUser(unittest.TestCase):
    '''
    test class that defines test cases for the user class behaviours
    '''

    def setUp(self):
        '''
        method to run before each test case
        :return:
        '''

        self.new_user = User("Erick","Mutua1234")

    def test_init(self):
        '''
        test case to test if an object is initialized properly
        :return:
        '''

        self.assertEqual(self.new_user.user_name, "Erick")
        self.assertEqual(self.new_user.user_password, "Mutua1234")


if __name__ == '__main__':
    unittest.main()
