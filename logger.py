from datetime import datetime
import logging
import os


class CustomizeLogger:
    def __init__(self, name: str = "sentiment_analysis") -> None:
        self.logger = self.__setup(name)


    def __setup(self, name: str) -> logging.Logger:
        # Crear un objeto de registro
        logger = logging.getLogger(name)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter("%(asctime)s|%(name)s|%(pathname)s|%(funcName)s|%(levelname)s|%(message)s")

        file_path = f"{datetime.now().strftime('%Y%m%d')}_errores.log"
        file_handler = logging.FileHandler(file_path)
        file_handler.setLevel(logging.ERROR)

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

        return logger