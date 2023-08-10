import os
import configparser

from logger import CustomizeLogger

logger = CustomizeLogger()


class OpenAI:
    api_key: str
    model: str
    max_tokens: int
    organization: str
    role: str


class CSV:
    file_name: str
    sep: str


class Excel:
    file_name: str
    sheet: str


class Settings:
    def __init__(self) -> None:
        self.openai: OpenAI = self.__read_ini("OPENIA", "OpenAI")
        self.csv: CSV = self.__read_ini("CSV", "CSV")
        self.excel: Excel = self.__read_ini("EXCEL", "Excel")
        self.directory: str = os.getcwd()


    def __read_ini(self, section_name: str, obj_class: any) -> any:
        try:
            config = configparser.ConfigParser()
            config.read(".ini")
            section = config.items(section_name)

            section_dict = {}
            for key, value in section:
                section_dict[key.lower()] = value

            new_class = type(obj_class, (object,), section_dict)

            return new_class
        except Exception as ex:
            logger.logger.error(str(ex))