import math
import numpy as np
import pandas as pd

from logger import CustomizeLogger

from file import IReadFile


logger = CustomizeLogger()


class CSV(IReadFile):
    def __init__(self, file_path: str, sep: str = ",", encoding="utf-8") -> None:
        self.__file_path = file_path
        self.__encoding = encoding
        self.__sep = sep


    @property
    def is_empty(self) -> bool:
        try:
            return self.read() is None or self.read().empty
        except Exception as ex:
            logger.logger.error(str(ex))
            raise ex


    def read(self) -> pd.DataFrame | None:
        try:
            return pd.read_csv(self.__file_path, sep=self.__sep, encoding=self.__encoding)
        except Exception as ex:
            logger.logger.error(str(ex))
            raise ex

    
    def split(self, size: int) -> list[pd.DataFrame]:
        try:
            if self.is_empty:
                raise ValueError("DataFrame no data.")
            
            df = self.read()
            total: int = df.shape[0]
            page: int = 0

            if size > total:
                page = 1
            else:
                page = math.ceil(total / size)

            df_split = np.array_split(df, page)

            return df_split
        except Exception as ex:
            logger.logger.error(str(ex))
            raise ex