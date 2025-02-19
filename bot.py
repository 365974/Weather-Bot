import logging
import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from config import TOKEN
from database import save_message, get_history

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def get_weather(city="Москва"):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        temp = data["current_condition"][0]["temp_C"]
        weather_desc = data["current_condition"][0]["weatherDesc"][0]["value"]
        return f"Погода в {city}: {temp}°C, {weather_desc}"
    else:
        return "Ошибка получения данных"

@dp.message(Command("start", "help"))
async def start_handler(message: Message):
    await message.answer("Привет! Отправь название города, и я скажу тебе погоду.")

@dp.message(Command("history"))
async def history_handler(message: Message):
    history = get_history(message.from_user.id)
    if history:
        await message.answer("Вот твоя история запросов:\n" + "\n".join(history[-5:]))
    else:
        await message.answer("История пока пустая.")

@dp.message()
async def weather_handler(message: Message):
    city = message.text.strip()
    weather = await get_weather(city)
    
    save_message(message.from_user.id, message.text)  # Сохраняем запрос
    await message.answer(weather)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    from database import init_db
    init_db()
    asyncio.run(main())

