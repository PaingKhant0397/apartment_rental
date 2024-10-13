from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database


class Contract_Agreement_Status:

    def __init__(self, contractAgreementStatusName: str, contractAgreementStatusID: int = None):

        self.__contractAgreementStatusID = contractAgreementStatusID
        self.__contractAgreementStatusName = contractAgreementStatusName

    @staticmethod
    def get(db: Database, contractAgreementStatusID: int) -> 'Contract_Agreement_Status':
        pass

    @staticmethod
    def all(db: Database) -> List['Contract_Agreement_Status']:
        pass
