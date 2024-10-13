from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from database import Database
    from .rental import Rental
    from .contract_agreement_status import Contract_Agreement_Status
    from datetime import date


class Contract_Agreement:

    def __init__(self, rental: Rental,  status: Contract_Agreement_Status, contractAgreement: str, contractAgreementDuration: str, contractAgreementIssuedDate: date, contractAgreementExpirationDate: date, contractAgreeementRequestedForRenewal: bool, contractAgreementID: int = None):

        self.__contractAgreementID = contractAgreementID
        self.__rental = rental
        self.__status = status
        self.__contractAgreement = contractAgreement
        self.__contractAgreementDuration = contractAgreementDuration
        self.__contractAgreementExpirationDate = contractAgreementExpirationDate
        self.__contractAgreementRequestedForRenewal = contractAgreeementRequestedForRenewal

    def save(self, db: Database) -> 'Contract_Agreement':
        pass

    @staticmethod
    def get(db: Database, contractAgreementID: int) -> 'Contract_Agreement':
        pass

    @staticmethod
    def delete(db: Database, contractAgreementID: int) -> None:
        pass

    @staticmethod
    def all(db: Database) -> List['Contract_Agreement']:
        pass
