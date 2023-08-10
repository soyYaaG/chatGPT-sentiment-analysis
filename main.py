from api.openai import ChatGPT
from file import FileType
from file.csv import CSV
from file.excel import Excel
from file.select_file import SelectFileType

from logger import CustomizeLogger
from settings import Settings


logger = CustomizeLogger()
settings = Settings()


# TODO: mejorar la complejidad algorítmica
def get_chat_gpt(get_file: CSV | Excel) -> str:
    data: str = ""
    df_split = get_file.split(50)
    chatgpt = ChatGPT()

    for i, df in enumerate(df_split):
        print(f"{i + 1} de {len(df_split)}")
        comments: str = "\n"

        for _, row in df.iterrows():
            comments += f"{row['ID']}|{row['COMENTARIO']}\n"
        
        try:
            response = chatgpt.get_reponse(comments)
            data += f"{response}\n"
        except Exception as ex:
            print("\tExcepción. Se continua con el proceso")
            print(f"\t\t{str(ex)}")
            continue

    return data


def main():
    get_file = SelectFileType().get_file(FileType.CSV)

    if get_file.is_empty:
        print("Sin datos")
        return
    
    result = get_chat_gpt(get_file)

    with open(f"{settings.directory}/result.txt", "w") as file:
        file.write(result)


if __name__ == "__main__":
    main()