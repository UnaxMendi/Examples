import imp
import unittest
from user import User

class UserTest(unittest.TestCase):
    def test_user_talks(self):
        juan_object = User("Juan", "j@j.com", 23, "London")
        ana_object = User('Ana', 'a', 56, 'other')
        print(juan_object)
        self.assertIsNotNone(juan_object)
        message = juan_object.talk()
        print(message)
        self.assertIsNotNone(message)
        self.assertTrue(message.index('Juan')>=0)
        message_from_ana=ana_object.talk()
        print(message_from_ana)
        self.assertTrue(message_from_ana.index('Ana')>=0)

    def test_user_says_its_adress(self):
        pedro_object = User('Pedro', 'p', 34, 'london')
        theadddress = pedro_object.saysAddress()
        self.assertTrue(theadddress.index('london')>=0)

    def NewTest(self):
        self.assertTrue(True) 