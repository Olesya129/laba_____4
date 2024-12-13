from pydantic import BaseModel  # Библиотека для валидации данных.
from datetime import datetime  # Для работы с датой и временем.

# Модель для данных, отправляемых при создании новой заметки.
class NoteCreate(BaseModel):
    text: str  # Поле для текста заметки.

# Модель для данных заметки, возвращаемых клиенту.
class Note(BaseModel):
    id: int  # Уникальный идентификатор заметки.
    text: str  # Текст заметки.
    created_at: str  # Время создания заметки в формате строки.
    updated_at: str  # Время последнего обновления заметки в формате строки.

# Модель для информации о времени создания и последнего обновления заметки.
class NoteInfo(BaseModel):
    created_at: datetime  # Время создания в формате datetime.
    updated_at: datetime  # Время последнего обновления в формате datetime.
