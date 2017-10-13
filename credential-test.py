import unittest
import pyperclip

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

    def test_display_all_credentials(self):

        self.assertEqual(Credential.display_credentials(), Credential.credential_list)

    def test_copy_account_password(self):

        self.new_credential.save_credential()
        Credential.copy_account_password("Erick1234")

        self.assertEqual(self.new_credential.account_password,pyperclip.paste())



if __name__ == '__main__':
    unittest.main()
