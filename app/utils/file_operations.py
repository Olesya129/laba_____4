import os  # Модуль для работы с файловой системой.

# Директория, в которой хранятся все файлы заметок.
NOTES_DIR = "notes"


# Функция для получения пути к файлу заметки по её идентификатору.
def get_note_path(note_id: int) -> str:
    """
    Возвращает полный путь к файлу заметки с заданным идентификатором.

    :param note_id: Уникальный идентификатор заметки.
    :return: Путь к файлу заметки.
    """
    # Создаёт путь в формате 'notes/<note_id>.json'
    return os.path.join(NOTES_DIR, f"{note_id}.json")
