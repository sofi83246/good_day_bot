from fastapi import FastAPI, Request
from aiogram import Bot, Dispatcher, types
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.webhook.aiohttp_server import SimpleRequestHandler
import asyncio
import os

API_TOKEN = os.getenv("API_TOKEN")
WEBHOOK_PATH = f"/bot/{API_TOKEN}"
WEBHOOK_URL = f"https://good_day_bot.onrender.com{WEBHOOK_PATH}"

bot = Bot(token=API_TOKEN)
dp = Dispatcher(storage=MemoryStorage())

app = FastAPI()

@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)

@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()

@app.post(WEBHOOK_PATH)
async def webhook(request: Request):
    update = types.Update(**await request.json())
    await dp.feed_update(bot, update)
    return {"status": "ok"}
