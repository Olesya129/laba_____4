import json
from fastapi import HTTPException

# Файл, где хранятся допустимые токены.
TOKENS_FILE = "tokens.json"


# Функция для проверки токена.
def verify_token(token: str):
    # Открываем файл с токенами в режиме чтения.
    with open(TOKENS_FILE, "r") as f:
        tokens = json.load(f)  # Загружаем токены из файла в виде словаря.

    # Проверяем, существует ли токен в списке допустимых значений.
    if token not in tokens.values():
        # Если токен недействителен, выбрасываем исключение HTTP с кодом 403 (Forbidden).
        raise HTTPException(status_code=403, detail="Invalid token")

    # Если токен валиден, возвращаем его.
    return token
