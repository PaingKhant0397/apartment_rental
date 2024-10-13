from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database
    from .rental import Rental
    from .invoice_status import Invoice_Status
    from datetime import date
    from decimal import Decimal


class Invoice:

    def __init__(self, rental: Rental,  status: Invoice_Status, waterBill: Decimal, electricityBill: Decimal, totalAmount: Decimal, issuedDate: date, dueDate: date, invoiceID: id = None):

        self.__invoiceID = invoiceID
        self.__status = status
        self.__rental = rental
        self.__electricityBill = electricityBill
        self.__waterBill = waterBill
        self.__totalAmount = totalAmount
        self.__issuedDate = issuedDate
        self.__dueDate == dueDate

    def save(self, db: Database) -> 'Invoice':
        pass

    @staticmethod
    def get(db: Database, contractAgreementID: int) -> 'Invoice':
        pass

    @staticmethod
    def delete(db: Database, contractAgreementID: int) -> None:
        pass

    @staticmethod
    def all(db: Database) -> List['Invoice']:
        pass
