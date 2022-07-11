import unittest
from user_manager import UserManager
from user import User

class UserManagerTest(unittest.TestCase):
    def test_addUser(self):
        user_manager=UserManager()
        new_user = User("Juan", "j@j.com", 23, "London")
        user_manager.addUser(new_user)
        print(len(user_manager.users))
        self.assertTrue(len(user_manager.users)>0)
        #self.assertIsNotNone(UserManager.users)

        user_manager.addUser(None)
        print(len(user_manager.users))
        self.assertTrue(len(user_manager.users)==1)

    def test_removeuser(self):
        user_manager=UserManager()
        new_user = User("Juan", "j@j.com", 23, "London")
        user_manager.addUser(new_user)
        print(len(user_manager.users))
        position = len(user_manager.users)-1
        user_manager.removeUser(position)
        print(len(user_manager.users))
        self.assertTrue(len(user_manager.users)==1)

if __name__ == '__main__':
    unittest.main()