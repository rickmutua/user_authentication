import unittest # importing the unittest module

from user import User # importing the user class


class TestUser(unittest.TestCase):

    def setUp(self):

        self.new_user = User("Erick","Mutua1234")

    def test_init(self):

        self.assertEqual(self.new_user.user_name, "Erick")
        self.assertEqual(self.new_user.user_password, "Mutua1234")

    def test_save_user(self):

        self.new_user.save_user()  # saving a new user
        self.assertEqual(len(User.user_list),1)

    def tearDown(self):
        User.user_list = []

    def test_save_multiple_users(self):

        self.new_user.save_user()
        test_user = User("Test", "user")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_user_exist(self):

        self.new_user.save_user()
        test_user = User("Test", "user")

        test_user.save_user()

        user_exists = User.user_exists("Erick", "Mutua1234")
        self.assertTrue(user_exists)



if __name__ == '__main__':
    unittest.main()
