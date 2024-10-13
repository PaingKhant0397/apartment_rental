from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database


class Admin():

    def __init__(self, adminID: int = None,  adminName: str = None, adminEmail: str = None, adminPassword: str = None):

        self.__adminID = adminID

        self.__adminName = adminName
        self.__adminEmail = adminEmail
        self.__adminPassword = adminPassword

    def save(self, db: Database) -> 'Admin':
        pass
        # query = "INSERT INTO Admin_table (AdminRoleID, adminName, adminEmail, adminPassword) VALUES (%s, %s, %s, %s) RETURNING adminID,AdminRoleID,adminName,adminEmail"
        # values = (self.AdminRoleID, self.adminName,
        #           self.adminEmail, self.adminPassword,)
        # return self.insert(query, values)

    @staticmethod
    def get(db: Database, AdminID: int) -> 'Admin':
        pass

    @staticmethod
    def delete(db: Database, AdminID: int) -> None:
        pass

    @staticmethod
    def all(db: Database,) -> List['Admin']:
        pass
        # query = """
        #             SELECT
        #                 u.AdminID,
        #                 u.adminName,
        #                 u.adminEmail,
        #                 ur.AdminRoleName
        #             FROM
        #                 Admin_table u
        #             JOIN
        #                 Admin_role ur
        #             ON
        #                 u.AdminRoleID = ur.AdminRoleID;
        #         """
        # return self.fetch_all(query)
