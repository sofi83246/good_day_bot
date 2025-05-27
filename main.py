import os
from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher
from aiogram.types import Update
from aiogram.methods import SetWebhook
import logging

API_TOKEN = os.getenv("API_TOKEN") or "ТВОЙ_ТОКЕН_СЮДА"  # временно можно вставить токен сюда

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
app = FastAPI()

WEBHOOK_PATH = "/webhook"
WEBHOOK_URL = "https://good-day-bot.onrender.com/webhook"
# === ВАЖНО: УСТАНОВКА ВЕБХУКА ===
@app.on_event("startup")
async def on_startup():
    logging.info("Устанавливаю вебхук...")
    await bot(SetWebhook(url=WEBHOOK_URL))
    logging.info("Вебхук установлен!")

# === УДАЛЕНИЕ ВЕБХУКА при остановке, по желанию ===
@app.on_event("shutdown")
async def on_shutdown():
    logging.info("Удаляю вебхук...")
    await bot.delete_webhook()

# === ОБРАБОТКА ВХОДЯЩИХ ОБНОВЛЕНИЙ ===
@app.post(WEBHOOK_PATH)
async def handle_webhook(request: Request):
    data = await request.json()
    update = Update.model_validate(data)
    await dp.feed_update(bot, update)
    return {"ok": True}
