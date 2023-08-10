import pandas as pd
from abc import ABC, abstractmethod
from enum import Enum, unique

from logger import CustomizeLogger


logger = CustomizeLogger()


class IReadFile(ABC):
    @abstractmethod
    def is_empty(self) -> bool:
        pass


    @abstractmethod
    def read(self) -> pd.DataFrame | None:
        pass


    @abstractmethod
    def split(self, size: int) -> list[pd.DataFrame]:
        pass


@unique
class FileType(Enum):
    EXCEL = "excel"
    CSV = "csv"