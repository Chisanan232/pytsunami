from smoothcrawler.persistence.database.strategy import BaseDatabaseConnection as _BaseDataBaseConnection

from abc import ABCMeta, ABC, abstractmethod
from typing import Tuple, TypeVar, Generic, Any, Optional


T = TypeVar("T")


class BaseDatabaseOperator(metaclass=ABCMeta):

    def __init__(self, conn_strategy: _BaseDataBaseConnection):
        self._conn_strategy = conn_strategy


    def initial(self) -> Generic[T]:
        pass


    @property
    def column_names(self) -> Generic[T]:
        raise NotImplementedError


    @property
    def row_count(self) -> Generic[T]:
        raise NotImplementedError


    def next(self) -> Generic[T]:
        raise NotImplementedError


    @abstractmethod
    def execute(self, operator: Any, params: Tuple = None, multi: bool = False) -> Generic[T]:
        pass


    def execute_many(self, operator: Any, seq_params=None) -> Generic[T]:
        raise NotImplementedError


    def fetch(self) -> Generic[T]:
        raise NotImplementedError


    def fetch_one(self) -> Generic[T]:
        raise NotImplementedError


    @abstractmethod
    def fetch_many(self, size: int = None) -> Generic[T]:
        pass


    def fetch_all(self) -> Generic[T]:
        raise NotImplementedError


    def reset(self) -> None:
        raise NotImplementedError


    @abstractmethod
    def close(self) -> Optional[Generic[T]]:
        pass



class DatabaseOperator(BaseDatabaseOperator, ABC):

    def initial(self, **kwargs) -> None:
        self._conn_strategy.connect_database(**kwargs)
        self._conn_strategy.build_cursor()


    def close(self) -> Optional[Generic[T]]:
        return self._conn_strategy.close()

