import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile

API_TOKEN = os.getenv("API_TOKEN") or "YOUR_BOT_TOKEN_HERE"
ADMIN_ID = os.getenv("ADMIN_ID") or "YOUR_ADMIN_ID_HERE"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="\ud83d\udcf1 Подробнее о приложении", callback_data="about_app")],
    [InlineKeyboardButton(text="\ud83d\udcbc Подробнее о франшизе", callback_data="franchise_step_1")],
    [InlineKeyboardButton(text="\ud83c\udfa5 Смотреть видео", callback_data="watch_video")],
    [InlineKeyboardButton(text="\ud83d\udcc4 Скачать презентацию", callback_data="download_presentation")],
    [InlineKeyboardButton(text="\ud83d\udcdd Оставить заявку", callback_data="send_request")]
])

@router.message(CommandStart())
async def start_handler(message: types.Message):
    text = (
        "\ud83d\udcf1 <b>Good Day</b> \u2014 это проект с различными направлениями и возможностями,\n"
        "но ключевым и объединяющим всё является наше <b>мобильное приложение</b>.\n\n"
        "Мы выбрали именно этот формат, ведь <b>смартфон \u2014 спутник каждого человека</b> \ud83d\udcf2"
    )
    await message.answer(text, parse_mode=ParseMode.HTML, reply_markup=main_menu)

# Franchise steps
franchise_steps = {
    "franchise_step_11": {
        "text": (
            "\ud83d\udcb5 <b>Стоимость франшизы:</b>\n\n"
            "<b>\u0422\u0430\u0440\u0438\u0444 \ab\u0411\u0430\u0437\u043e\u0432\u044b\u0439\bb</b> \u2014 200 000 \u0440\u0443\u0431.\n"
            "Роялти: 15%\n"
            "Первые 6 месяцев \u2014 без роялти.\n\n"
            "<b>\u0422\u0430\u0440\u0438\u0444 \ab\u0421\u0442\u0430\u043d\u0434\u0430\u0440\u0442\bb</b> \u2014 300 000 \u0440\u0443\u0431.\n"
            "Роялти: 10%\n"
            "Первые 9 месяцев \u2014 без роялти.\n\n"
            "<b>\u0422\u0430\u0440\u0438\u0444 \ab\u0411\u0438\u0437\u043d\u0435\u0441\bb</b> \u2014 400 000 \u0440\u0443\u0431.\n"
            "Роялти: 5%\n"
            "Без роялти весь первый год.\n\n"
            "<b>\u0422\u0430\u0440\u0438\u0444 \ab\u041b\u0430\u0439\u0442\bb</b> \u2014 100 000 \u0440\u0443\u0431.\n"
            "\u0421\u0442\u0430\u0440\u0442\u043e\u0432\u044b\u0435 \u0438\u043d\u0432\u0435\u0441\u0442\u0438\u0446\u0438\u0438 \u0443\u0432\u0435\u043b\u0438\u0447\u0438\u0432\u0430\u044e\u0442\u0441\u044f \u0434\u043e 200 000 \u0440\u0443\u0431. \u0434\u043b\u044f \u0430\u0434\u043c. \u0446\u0435\u043d\u0442\u0440\u043e\u0432.\n"
            "Минимум два франчайзи на город.\n\n"
            "<b>\u041e\u043a\u0443\u043f\u0430\u0435\u043c\u043e\u0441\u0442\u044c</b>: от 2 до 4 месяцев.\n\n"
            "<b>\u0413\u0430\u0440\u0430\u043d\u0442\u0438\u044f:</b> возврат вложений при непредвидённых обстоятельствах."
        ),
        "next": None
    }
}
