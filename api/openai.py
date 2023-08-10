import openai

from logger import CustomizeLogger
from settings import Settings


logger = CustomizeLogger()
settings = Settings()


class ChatGPT:
    def __get_prompt(self, comment: str) -> str:
        with open(f"{settings.directory}/api/prompt.txt") as file:
            return str.format(file.read(), comment)


    def __get_message(self, choices: any) -> str:
        message = ""

        for choice in choices:
            message += choice.message.content

        return message


    def get_reponse(self, comment: str) -> str:
        openai.api_key = settings.openai.api_key
        openai.organization = settings.openai.organization

        try:
            response = openai.ChatCompletion.create(
                model=settings.openai.model,
                messages=[{
                    "role": settings.openai.role,
                    "content": self.__get_prompt(comment)
                }]
            )

            return self.__get_message(response.choices)
        except Exception as ex:
            logger.logger.error(str(ex))
            raise ex