from file import FileType
from file.csv import CSV
from file.excel import Excel

from logger import CustomizeLogger
from settings import Settings


logger = CustomizeLogger()
settings = Settings()


class SelectFileType:
    @staticmethod
    def get_file(file_type: FileType):
        if file_type == FileType.EXCEL:
            return Excel(f"{settings.directory}/{settings.excel.file_name}", settings.excel.sheet)
        elif file_type == FileType.CSV:
            return CSV(f"{settings.directory}/{settings.csv.file_name}", sep=settings.csv.sep)