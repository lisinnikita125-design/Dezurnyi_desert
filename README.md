# desert_bot

Простой Telegram-бот на `python-telegram-bot` (polling).

## Важно про токен

Не храните токен в коде и не публикуйте его. Если вы уже вставляли токен в чат/репозиторий — **отзовите его в BotFather** и выпустите новый.

## Установка (Windows / PowerShell)

```powershell
cd "c:\Users\acer\Desktop\desert_bot"
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Настройка токена

Задайте переменную окружения (после этого откройте новый терминал):

```powershell
setx TELEGRAM_BOT_TOKEN "ВАШ_ТОКЕН_ОТ_BOTFATHER"
```

Проверить, что переменная видна в новом терминале:

```powershell
echo $env:TELEGRAM_BOT_TOKEN
```

## Запуск

```powershell
python bot.py
```

## Команды бота

- `/start` — приветствие и подсказка
- `/add [N]` — добавить к счётчику (по умолчанию 1)
- `/count` — показать счётчик
- `/reset` — сбросить счётчик

