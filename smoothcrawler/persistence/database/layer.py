from smoothcrawler.persistence.interface import DataPersistenceLayer
from smoothcrawler.persistence.database.operator import DatabaseOperator

from abc import ABCMeta, ABC, abstractmethod
from typing import Tuple, TypeVar, Generic, Any, Optional


T = TypeVar("T")


class DatabaseAccessObject(DataPersistenceLayer, ABC):

    def __init__(self, **kwargs):
        super(DatabaseAccessObject, self).__init__(**kwargs)



class CrawlerDao(DatabaseAccessObject):

    @property
    @abstractmethod
    def database_opt(self) -> DatabaseOperator:
        pass


    def execute(self, operator: Any, params: Tuple = None, multi: bool = False) -> Generic[T]:
        return self.database_opt.execute(operator=operator, params=params, multi=multi)


    def execute_many(self, operator: Any, seq_params: Tuple = None) -> Generic[T]:
        return self.database_opt.execute_many(operator=operator, seq_params=seq_params)


    def fetch_many(self, size: int = None) -> Generic[T]:
        return self.database_opt.fetch_many(size=size)


    def close(self) -> Optional[Generic[T]]:
        return self.database_opt.close()

