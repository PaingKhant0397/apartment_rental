import unittest
from database import Database
from models.user_role import User_Role
# Ensure this has the correct test DB connection parameters
from config import TEST_CONNECTION_PARAMS


class TestUserRole(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db = Database(TEST_CONNECTION_PARAMS)

    def setUp(self):
        self.db.execute_query(
            "INSERT INTO user_role (userRoleID, userRoleName) VALUES (%s, %s);", (1, 'normal'))
        self.db.execute_query(
            "INSERT INTO user_role (userRoleID, userRoleName) VALUES (%s, %s);", (2, 'tenant'))

    def tearDown(self):
        self.db.execute_query(
            "TRUNCATE TABLE user_role RESTART IDENTITY CASCADE;")

    @classmethod
    def tearDownClass(cls):
        cls.db = None

    def test_initialization(self):
        """ Testing of User_Role class initialization."""
        user_role = User_Role(userRoleID=1, userRoleName="normal")
        self.assertEqual(user_role.get_userRoleID(), 1)
        self.assertEqual(user_role.get_userRoleName(), "normal")

    def test_to_dict(self):
        """ Testing of User_Role class converting to dict"""
        user_role = User_Role(userRoleID=1, userRoleName="normal")
        expected_dict = {
            "userRoleID": 1,
            "userRoleName": "normal",
        }
        self.assertEqual(user_role.to_dict(), expected_dict)

    def test_get_success(self):
        """ Testing of User_Role class getting user role by name"""
        user_role = User_Role.get(self.db, 1)
        self.assertIsInstance(user_role, User_Role)
        self.assertEqual(user_role.get_userRoleID(), 1)
        self.assertEqual(user_role.get_userRoleName(), 'normal')

    def test_get_not_found(self):
        user_role = User_Role.get(self.db, 999)  # Assuming 999 does not exist
        self.assertIsNone(user_role)

    def test_all(self):
        """Test retrieving all user roles from the database."""
        user_roles = User_Role.all(self.db)

        # Assert the results
        self.assertEqual(len(user_roles), 2)
        self.assertEqual(user_roles[0].get_userRoleID(), 1)
        self.assertEqual(user_roles[0].get_userRoleName(), 'normal')
        self.assertEqual(user_roles[1].get_userRoleID(), 2)
        self.assertEqual(user_roles[1].get_userRoleName(), 'tenant')


if __name__ == '__main__':
    unittest.main()
