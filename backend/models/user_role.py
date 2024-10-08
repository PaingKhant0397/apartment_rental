from .database import Database


class User_Role(Database):

    def __init__(self, userRoleName=None):
        super().__init__()
        self.userRoleName = userRoleName

    def insert(self):
        query = "INSERT INTO user_role(userRoleName) VALUES(%s) RETURNING userRoleID,userRoleName;"
        values = (self.userRoleName,)
        return self.insert(query, values)

    def all(self):
        query = "SELECT * FROM user_role;"
        return self.fetch_all(query)
