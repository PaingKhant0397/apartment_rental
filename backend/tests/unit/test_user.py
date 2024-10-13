import unittest
from models.user import User
from models.user_role import User_Role
from database import Database
from config import TEST_CONNECTION_PARAMS


class TestUser(unittest.TestCase):

    def setUp(self):
        # Create a mock User_Role instance
        self.mock_role = User_Role(userRoleID=1, userRoleName="Admin")
        self.user = User(role=self.mock_role, userID=1, userName="test_user",
                         userEmail="test@example.com", userPassword="securepassword")

    def test_initialization(self):
        self.assertEqual(self.user.get_userPassword(), "securepassword")
        self.assertEqual(self.user.to_dict(), {
            "userID": 1,
            "role": {
                "userRoleID": 1,
                "userRoleName": "Admin"
            },
            "userName": "test_user",
            "userEmail": "test@example.com"
        })

    def test_to_dict(self):
        expected_dict = {
            "userID": 1,
            "role": {
                "userRoleID": 1,
                "userRoleName": "Admin"
            },
            "userName": "test_user",
            "userEmail": "test@example.com"
        }
        self.assertEqual(self.user.to_dict(), expected_dict)

    def test_set_user_password(self):
        self.user.set_userPassword("newpassword")
        self.assertEqual(self.user.get_userPassword(), "newpassword")


class TestUserRoleIntegration(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Set up a real database connection and any necessary test data
        cls.db = Database(TEST_CONNECTION_PARAMS)
        # Setup the necessary roles and users in the database for integration tests
        cls.user_role = User_Role(userRoleID=1, userRoleName="Admin")
        cls.db.execute_query(
            "INSERT INTO user_role (userRoleID, userRoleName) VALUES (%s, %s);", (1, 'Admin'))

        cls.user = User(role=cls.user_role, userName="test_user",
                        userEmail="test@example.com", userPassword="securepassword")

    def test_insert_user(self):
        """Test if the insert method successfully adds a user to the database."""
        inserted_user = self.user.insert(self.db)
        self.assertIsNotNone(
            inserted_user, "User should have been inserted successfully")
        self.assertEqual(inserted_user.userName,
                         self.user.userName, "Usernames should match")
        self.assertEqual(inserted_user.userEmail,
                         self.user.userEmail, "User emails should match")

        # Additionally, verify that the user exists in the database
        query = "SELECT * FROM user_table WHERE userName = %s;"
        result = self.db.fetch_one(query, (self.user.userName,))
        self.assertIsNotNone(result, "User should exist in the database")
        self.assertEqual(result['userName'], self.user.userName,
                         "Usernames should match in the database")
        self.assertEqual(result['userEmail'], self.user.userEmail,
                         "User emails should match in the database")

    def test_get_user_by_username(self):
        retrieved_user = User.get(self.db, "test_user")
        self.assertIsNotNone(retrieved_user)
        self.assertEqual(retrieved_user.userName, "test_user")

    @classmethod
    def tearDownClass(cls):
        # Clean up the test data from the database
        cls.db.execute_query(
            "DELETE FROM user_table WHERE userName = %s;", ("test_user",))
        cls.db.execute_query(
            "DELETE FROM user_role WHERE userRoleID = %s;", (1,))
        cls.db = None  # Close or clean up your DB connection if necessary


if __name__ == '__main__':
    unittest.main()
