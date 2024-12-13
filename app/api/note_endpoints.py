from fastapi import APIRouter, Header
# APIRouter позволяет создавать маршруты для API, Header используется для работы с заголовками запросов.

from app.auth.token_auth import verify_token
# verify_token – функция для проверки валидности токена, обеспечивающая авторизацию.

from app.controller.note_service import (
    create_note_service, get_note_service,
    get_note_info_service, update_note_service,
    delete_note_service, list_notes_service
)
# Импортируем сервисы для работы с заметками: создание, получение, обновление, удаление и список заметок.

from app.models.note import Note, NoteInfo, NoteCreate
# Импортируем модели данных для заметок: Note (полная информация), NoteInfo (время создания/изменения), NoteCreate (данные для создания заметки).

# Создаём экземпляр маршрутизатора для API.
router = APIRouter()

# Маршрут для создания заметки.
@router.post("/notes", response_model=Note)
def create_note(note: NoteCreate, authorization: str = Header(...)):
    # Получаем токен из заголовка Authorization.
    token = authorization.replace("Bearer ", "")
    verify_token(token)  # Проверяем валидность токена.
    print("Пришёл запрос с данными токена: " + token)  # Логируем токен (для отладки).
    return create_note_service(note.text)  # Вызываем сервис для создания заметки и возвращаем результат.

# Маршрут для получения текста заметки по её ID.
@router.get("/notes/{note_id}", response_model=Note)
def get_note(note_id: int, authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    verify_token(token)
    return get_note_service(note_id)  # Вызываем сервис для получения текста заметки.

# Маршрут для получения информации о времени создания и последнего изменения заметки.
@router.get("/notes/{note_id}/info", response_model=NoteInfo)
def get_note_info(note_id: int, authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    verify_token(token)
    return get_note_info_service(note_id)  # Вызываем сервис для получения информации о заметке.

# Маршрут для обновления текста заметки.
@router.patch("/notes/{note_id}", response_model=Note)
def update_note(note_id: int, note: NoteCreate, authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    verify_token(token)
    return update_note_service(note_id, note.text)  # Вызываем сервис для обновления текста заметки.

# Маршрут для удаления заметки по её ID.
@router.delete("/notes/{note_id}")
def delete_note(note_id: int, authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    verify_token(token)
    return delete_note_service(note_id)  # Вызываем сервис для удаления заметки.

# Маршрут для получения списка всех ID заметок.
@router.get("/notes", response_model=dict)
def list_notes(authorization: str = Header(...)):
    token = authorization.replace("Bearer ", "")
    verify_token(token)
    return list_notes_service()  # Вызываем сервис для получения списка ID всех заметок.
