import unittest
# import pyperclip

from credential import Credential


class TestCredential(unittest.TestCase):

    def setUp(self):

        self.new_credential = Credential("Facebook", "Erick1234", "erick@mutua.com")

    def test_init(self):

        self.assertEqual(self.new_credential.account_name,"Facebook")
        self.assertEqual(self.new_credential.account_password, "Erick1234")
        self.assertEqual(self.new_credential.account_email, "erick@mutua.com")

    def test_save_credential(self):

        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1)

    def tearDown(self):
        Credential.credential_list = []

    def test_save_multiple_credentials(self):

        self.new_credential.save_credential()

        test_credential = Credential("Test", "user", "test@user.com")
        test_credential.save_credential()

        self.assertEqual(len(Credential.credential_list),2)

    def test_credential_exists(self):

        self.new_credential.save_credential()

        test_credential = Credential("Test", "user", "test@user.com")

        test_credential.save_credential()

        credential_exists = Credential.credential_exist("Test", "user")

        self.assertTrue(credential_exists)

    def test_delete_credential(self):

        self.new_credential.save_credential()
        test_credential = Credential("Test", "user", "test@user.com")

        test_credential.save_credential()
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list))

    def test_display_all_credentials(self):

        self.assertEqual(Credential.display_credentials(), Credential.credential_list)

    # def test_credential_exists(self):
    #     self.new_credential.save_credential()
    #
    #     test_credential = Credential("Test", "user", "test@user.com")
    #
    #     test_credential.save_credential()
    #
    #     found_credential = Credential.find_by_account_name(test_credential.account_name)
    #     self.assertEqual(found_credential.account.password, test_credential.account_password)

    # def test_copy_credential(self,):
    #
    #     self.new_credential.save_credential()
    #     Credential.copy_credential("Facebook")
    #
    #     self.assertEqual(self.new_credential.credential,pyperclip.paste())
    #
    # def test_auto_generate_password(self):
    #
    #     auto_generate_password = self.new_credential.password_autogeneration()
    #     self.assertEqual(len(auto_generate_password), 8)



if __name__ == '__main__':
    unittest.main()
