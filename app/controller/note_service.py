import os
import json
from datetime import datetime
from app.utils.file_operations import get_note_path  # Функция для получения пути к файлу заметки.
from app.models.note import Note, NoteInfo  # Импортируем модели для валидации данных.
from fastapi import HTTPException

# Директория, в которой хранятся файлы заметок.
NOTES_DIR = "notes"

# Функция для создания новой заметки.
def create_note_service(text: str) -> Note:
    # Если директория для заметок не существует, создаем её.
    if not os.path.exists(NOTES_DIR):
        os.makedirs(NOTES_DIR)

    # Генерируем новый ID для заметки на основе количества файлов в директории.
    note_id = len(os.listdir(NOTES_DIR)) + 1

    # Формируем данные заметки.
    note_data = {
        "id": note_id,
        "text": text,
        "created_at": datetime.now().isoformat(),  # Время создания в формате ISO.
        "updated_at": datetime.now().isoformat()  # Время последнего обновления.
    }

    # Сохраняем данные заметки в файл.
    with open(get_note_path(note_id), "w") as f:
        json.dump(note_data, f)

    # Возвращаем объект Note, созданный на основе данных.
    return Note(**note_data)

# Функция для получения текста заметки по её ID.
def get_note_service(note_id: int) -> Note:
    try:
        # Открываем файл с заметкой и загружаем её данные.
        with open(get_note_path(note_id), "r") as f:
            note_data = json.load(f)
        return Note(**note_data)  # Возвращаем объект Note.
    except FileNotFoundError:
        # Если файл не найден, выбрасываем исключение с кодом 404.
        raise HTTPException(status_code=404, detail="Note not found")

# Функция для получения информации о времени создания и обновления заметки.
def get_note_info_service(note_id: int) -> NoteInfo:
    # Получаем текст заметки.
    note = get_note_service(note_id)
    # Возвращаем только информацию о времени.
    return NoteInfo(created_at=note.created_at, updated_at=note.updated_at)

# Функция для обновления текста заметки.
def update_note_service(note_id: int, text: str) -> Note:
    # Загружаем существующую заметку.
    note = get_note_service(note_id)
    # Обновляем текст и время последнего изменения.
    note.text = text
    note.updated_at = datetime.now().isoformat()

    # Сохраняем обновленные данные заметки обратно в файл.
    with open(get_note_path(note_id), "w") as f:
        json.dump(note.dict(), f)  # Сериализуем объект Note в JSON.

    return note

# Функция для удаления заметки.
def delete_note_service(note_id: int):
    try:
        # Удаляем файл заметки.
        os.remove(get_note_path(note_id))
    except FileNotFoundError:
        # Если файл не найден, выбрасываем исключение с кодом 404.
        raise HTTPException(status_code=404, detail="Note not found")

# Функция для получения списка всех ID заметок.
def list_notes_service() -> dict:
    # Получаем список всех файлов в директории заметок.
    notes = os.listdir(NOTES_DIR)
    # Создаем словарь, где ключи — порядковые номера, а значения — ID заметок.
    note_ids = {i: int(note.split(".")[0]) for i, note in enumerate(notes)}
    return note_ids
