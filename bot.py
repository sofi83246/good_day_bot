import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile

API_TOKEN = os.getenv("API_TOKEN")
ADMIN_ID = os.getenv("ADMIN_ID")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

# Главное меню
main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📱 Узнать о приложении", callback_data="about_app")],
    [InlineKeyboardButton(text="💼 Подробнее о франшизе", callback_data="about_franchise")],
    [InlineKeyboardButton(text="🎥 Смотреть видео", callback_data="watch_video")],
    [InlineKeyboardButton(text="📄 Скачать презентацию", callback_data="download_presentation")],
    [InlineKeyboardButton(text="📝 Оставить заявку", callback_data="send_request")]
])

# Команды Telegram меню (слева от поля ввода)
@dp.startup()
async def setup_bot_commands(bot: Bot):
    commands = [
        types.BotCommand(command="menu", description="Главное меню"),
        types.BotCommand(command="app", description="О приложении"),
        types.BotCommand(command="franchise", description="О франшизе"),
        types.BotCommand(command="presentation", description="Скачать презентацию"),
        types.BotCommand(command="video", description="Смотреть видео"),
        types.BotCommand(command="apply", description="Оставить заявку")
    ]
    await bot.set_my_commands(commands)

# Главное меню
@router.message(Command("menu"))
async def menu_command(message: types.Message):
    await message.answer("⬇ Главное меню:", reply_markup=main_menu)

# О приложении
@router.message(Command("app"))
@router.callback_query(F.data == "about_app")
async def about_app(event):
    msg = event.message if isinstance(event, types.CallbackQuery) else event
    await msg.answer(
        "📱 В приложении Good Day:\n"
        "• Скидки и акции в городе\n"
        "• Реклама для бизнесов\n"
        "• Удобный поиск и фильтры\n\n"
        "🔥 Идеально подходит для пользователей и предпринимателей.",
        reply_markup=main_menu
    )
    if isinstance(event, types.CallbackQuery): await event.answer()

# О франшизе
@router.message(Command("franchise"))
@router.callback_query(F.data == "about_franchise")
async def about_franchise(event):
    msg = event.message if isinstance(event, types.CallbackQuery) else event
    await msg.answer(
        "💼 Франшиза Good Day — это:\n"
        "• Минимальные риски\n"
        "• Эксклюзивность в регионе\n"
        "• Готовый IT-продукт\n"
        "• Поддержка, обучение и маркетинг\n\n"
        "Ты зарабатываешь на подключении бизнеса к рекламным пакетам.\n"
        "Мы помогаем тебе на каждом этапе запуска.",
        reply_markup=main_menu
    )
    if isinstance(event, types.CallbackQuery): await event.answer()

# Скачать презентацию
@router.message(Command("presentation"))
@router.callback_query(F.data == "download_presentation")
async def send_presentation(event):
    msg = event.message if isinstance(event, types.CallbackQuery) else event
    document = FSInputFile("presentation.pdf")
    await msg.answer_document(document, caption="📄 Презентация франшизы Good Day", reply_markup=main_menu)
    if isinstance(event, types.CallbackQuery): await event.answer()

# Смотреть видео
@router.message(Command("video"))
@router.callback_query(F.data == "watch_video")
async def send_video(event):
    msg = event.message if isinstance(event, types.CallbackQuery) else event
    video = FSInputFile("intro_video.mp4")
    await msg.answer_video(video=video, caption="🎥 Видео-презентация от основателя", reply_markup=main_menu)
    if isinstance(event, types.CallbackQuery): await event.answer()

# Оставить заявку
@router.message(Command("apply"))
@router.callback_query(F.data == "send_request")
async def send_request(event):
    user = event.from_user
    msg = event.message if isinstance(event, types.CallbackQuery) else event
    text = (
        f"📬 Новая заявка!\n\n"
        f"Имя: {user.full_name}\n"
        f"Юзернейм: @{user.username if user.username else 'нет'}\n"
        f"ID: {user.id}"
    )
    if ADMIN_ID:
        await bot.send_message(chat_id=int(ADMIN_ID), text=text)
    await msg.answer("✅ Заявка отправлена! Мы свяжемся с тобой в ближайшее время.", reply_markup=main_menu)
    if isinstance(event, types.CallbackQuery): await event.answer()

# Запуск бота
async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
