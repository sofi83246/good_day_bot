import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile

# Можно указать вручную для тестов (лучше использовать переменные окружения)
API_TOKEN = os.getenv("API_TOKEN") 
ADMIN_ID = os.getenv("ADMIN_ID")

# Настройка логгера
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()
dp.include_router(router)

# Главное меню
main_menu = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="📱 Подробнее о приложении", callback_data="about_app")],
    [InlineKeyboardButton(text="💼 Подробнее о франшизе", callback_data="about_franchise")],
    [InlineKeyboardButton(text="🎥 Смотреть видео", callback_data="watch_video")],
    [InlineKeyboardButton(text="📄 Скачать презентацию", callback_data="download_presentation")],
    [InlineKeyboardButton(text="📝 Оставить заявку", callback_data="send_request")]
])

# Стартовое сообщение
@router.message(CommandStart())
async def start_handler(message: types.Message):
    text = (
        "📱 <b>Good Day</b> — это проект с различными направлениями и возможностями,\n"
        "но ключевым и объединяющим всё является наше <b>мобильное приложение</b>.\n\n"
        "Мы выбрали именно этот формат, ведь <b>смартфон — спутник каждого человека</b> 📲"
    )
    await message.answer(text, parse_mode=ParseMode.HTML, reply_markup=main_menu)

# Подробнее о приложении
@router.callback_query(F.data == "about_app")
async def about_app(callback: types.CallbackQuery):
    await callback.message.answer(
        "📱 В приложении Good Day:\n"
        "• Скидки и акции в городе\n"
        "• Реклама для бизнесов\n"
        "• Удобный поиск и фильтры\n\n"
        "🔥 Идеально подходит для пользователей и предпринимателей.",
        reply_markup=main_menu
    )
    await callback.answer()

# Подробнее о франшизе
@router.callback_query(F.data == "about_franchise")
async def about_franchise(callback: types.CallbackQuery):
    await callback.message.answer(
        "💼 Франшиза Good Day — это:\n"
        "• Минимальные риски\n"
        "• Эксклюзивность в регионе\n"
        "• Готовый IT-продукт\n"
        "• Поддержка, обучение и маркетинг\n\n"
        "Ты зарабатываешь на подключении бизнеса к рекламным пакетам.\n"
        "Мы помогаем тебе на каждом этапе запуска.",
        reply_markup=main_menu
    )
    await callback.answer()

# Отправка видео
@router.callback_query(F.data == "watch_video")
async def send_video(callback: types.CallbackQuery):
    video = FSInputFile("intro.mp4")
    await callback.message.answer_video(video=video, caption="🎬 Посмотри короткое видео о проекте Good Day!", reply_markup=main_menu)
    await callback.answer()

# Отправка презентации
@router.callback_query(F.data == "download_presentation")
async def send_presentation(callback: types.CallbackQuery):
    doc = FSInputFile("presentation.pdf")
    await callback.message.answer_document(document=doc, caption="📄 Презентация франшизы Good Day", reply_markup=main_menu)
    await callback.answer()

# Оставить заявку
@router.callback_query(F.data == "send_request")
async def send_request(callback: types.CallbackQuery):
    user = callback.from_user
    text = (
        f"📬 Новая заявка!\n\n"
        f"Имя: {user.full_name}\n"
        f"Юзернейм: @{user.username if user.username else 'нет'}\n"
        f"ID: {user.id}"
    )
    if ADMIN_ID:
        await bot.send_message(chat_id=int(ADMIN_ID), text=text)
    await callback.message.answer("✅ Заявка отправлена! Мы свяжемся с тобой в ближайшее время.", reply_markup=main_menu)
    await callback.answer()

# Запуск бота
async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
