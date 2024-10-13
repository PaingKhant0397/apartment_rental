from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database


class Invoice_Status:

    def __init__(self, invoiceStatusName: str, invoiceStatusID: int = None):

        self.__invoiceStatusID = invoiceStatusID
        self.__invoiceStatusName = invoiceStatusName

    @staticmethod
    def get(db: Database, invoiceStatusID: int) -> 'Invoice_Status':
        pass

    @staticmethod
    def all(db: Database) -> List['Invoice_Status']:
        pass
