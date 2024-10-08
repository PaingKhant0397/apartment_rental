from .database import Database


class User(Database):

    def __init__(self, userRoleID=None, userName=None, userEmail=None, userPassword=None):

        super().__init__()

        self.userRoleID = userRoleID
        self.userName = userName
        self.userEmail = userEmail
        self.userPassword = userPassword

    def insert(self):
        query = "INSERT INTO user_table (userRoleID, userName, userEmail, userPassword) VALUES (%s, %s, %s, %s) RETURNING userID,userRoleID,userName,userEmail"
        values = (self.userRoleID, self.userName,
                  self.userEmail, self.userPassword,)
        return self.insert(query, values)

    def all(self):
        query = """
                    SELECT 
                        u.userID,
                        u.userName,
                        u.userEmail,
                        ur.userRoleName
                    FROM 
                        user_table u 
                    JOIN 
                        user_role ur 
                    ON 
                        u.userRoleID = ur.userRoleID;
                """
        return self.fetch_all(query)
