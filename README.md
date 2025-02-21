# Telegram Weather Bot

Этот бот позволяет получать актуальную погоду в любом городе, используя сервис `wttr.in`.  
Он написан на `Python` с использованием библиотеки `aiogram` и поддерживает сохранение истории запросов в `SQLite`.

## Возможности
- Получение погоды по названию города.
- Сохранение истории запросов пользователя.
- Поддержка команд `/start`, `/help`, `/history`.

## Установка и запуск

### Клонирование репозитория

```bash
git clone https://github.com/365974/weather-bot.git
cd weather-bot
```
## Установка зависимостей

Создай виртуальное окружение и установи зависимости:
```bash
python3 -m venv mybot_env
source mybot_env/bin/activate
pip install -r requirements.txt
```

## Настройка бота

Создай файл config.py и добавь в него токен бота:
```python
TOKEN = "ТВОЙ_ТОКЕН_БОТА"
```

## Инициализация базы данных

Запусти команду:
```bash
python database.py
```

Это создаст базу данных history.db.

## Запуск бота
```bash
python bot.py
```
## Команды бота

    /start — запустить бота.
    /help — получить справку.
    /history — посмотреть историю своих запросов.

## Автозапуск бота через systemd

Если хочешь, чтобы бот запускался автоматически:
Создай файл /etc/systemd/system/weather-bot.service:

```bash
[Unit]
Description=Telegram Weather Bot
After=network.target

[Service]
User=your_user
WorkingDirectory=/home/your_user/weather-bot
ExecStart=/home/your_user/mybot_env/bin/python /home/your_user/weather-bot/bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

## Активируй службу:
```bash
sudo systemctl daemon-reload
sudo systemctl enable weather-bot
sudo systemctl start weather-bot
```

## Лицензия

Проект распространяется под MIT License.
