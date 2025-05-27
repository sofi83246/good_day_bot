import os
import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, FSInputFile
from keep_alive import keep_alive

# Установите свои значения или используйте переменные окружения
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
    [InlineKeyboardButton(text="💼 Подробнее о франшизе", callback_data="franchise_step_1")],
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
    text = (
        "📱 <b>Good Day</b> — это мобильное приложение, которое помогает пользователям экономить время и деньги.\n\n"
        "👥 <b>Для пользователей:</b>\n"
        "• Уникальные скидки и акции\n"
        "• Электронная карта лояльности\n"
        "• Дисконтные карты\n"
        "• Онлайн-запись к мастерам\n"
        "• Интерактивная карта с партнёрами\n\n"
        "🏢 <b>Для бизнеса:</b>\n"
        "• Эффективный канал продвижения\n"
        "• Программа лояльности\n"
        "• Push-уведомления и сторис\n"
        "• Аналитика и отчёты\n\n"
        "📊 На данный момент:\n"
        "• 23 000+ скачиваний приложения\n"
        "• 15 500+ активных пользователей\n"
        "• 2 200+ бизнесов-партнёров"
    )
    await callback.message.answer(text, parse_mode=ParseMode.HTML, reply_markup=main_menu)
    await callback.answer()

# Пошаговая презентация франшизы
franchise_steps = {
    "franchise_step_1": {
        "text": (
            "💼 <b>Преимущества франшизы Good Day:</b>\n\n"
            "• Быстрая окупаемость: 2–4 месяца\n"
            "• Эксклюзивность в регионе\n"
            "• Готовое IT-решение стоимостью более $40 000\n"
            "• Постоянная поддержка и обучение\n"
            "• Работа без офиса и персонала\n"
            "• Потенциальный доход от 4 000 BYN в месяц"
        ),
        "next": "franchise_step_2"
    },
    "franchise_step_2": {
        "text": (
            "🎯 <b>Наша цель:</b>\n\n"
            "Собрать дружную и сплочённую команду франчайзи по всем городам России и Беларуси, "
            "чтобы вместе развивать проект и приносить пользу пользователям и бизнесу."
        ),
        "next": "franchise_step_3"
    },
    "franchise_step_3": {
        "text": (
            "📍 <b>Эксклюзивность:</b>\n\n"
            "Каждый франчайзи получает эксклюзивное право представлять Good Day в своём городе. "
            "Это означает отсутствие конкуренции внутри сети и полную поддержку со стороны головного офиса."
        ),
        "next": "franchise_step_4"
    },
    "franchise_step_4": {
        "text": (
            "🤝 <b>Система Win-Win-Win:</b>\n\n"
            "• Пользователь получает выгодные предложения и экономит деньги.\n"
            "• Бизнес привлекает новых клиентов и увеличивает продажи.\n"
            "• Франчайзи зарабатывает на подписках и рекламе.\n\n"
            "Все стороны выигрывают!"
        ),
        "next": "franchise_step_5"
    },
    "franchise_step_5": {
        "text": (
            "💰 <b>Как зарабатывает франчайзи:</b>\n\n"
            "• Подписки пользователей на приложение\n"
            "• Платные сторис и push-уведомления\n"
            "• Продвижение партнёров в категории «Популярное»\n"
            "• Размещение акций и событий в разделе новостей"
        ),
        "next": "franchise_step_6"
    },
    "franchise_step_6": {
        "text": (
            "🧑‍💼 <b>У нашего франчайзи всего 2 задачи:</b>\n\n"
            "1. Подключать местные бизнесы к платформе.\n"
            "2. Продвигать приложение среди жителей города.\n\n"
            "Всё остальное — техническая поддержка, обновления, маркетинг — берёт на себя команда Good Day."
        ),
        "next": "franchise_step_7"
    },
    "franchise_step_7": {
        "text": (
            "🎁 <b>Что вы получите по нашей франшизе:</b>\n\n"
            "• Готовое мобильное приложение\n"
            "• Персонального куратора\n"
            "• Обучение и инструкции\n"
            "• Маркетинговые материалы\n"
            "• Поддержку 24/7\n"
            "• Возможность проводить мероприятия (фестивали, квесты, шоу)"
        ),
        "next": "franchise_step_8"
    },
    "franchise_step_8": {
        "text": (
            "🚀 <b>Этапы запуска:</b>\n\n"
            "1. Подписание договора\n"
            "2. Обучение и знакомство с платформой\n"
            "3. Подключение первых бизнесов\n"
            "4. Запуск рекламной кампании\n"
            "5. Проведение первого мероприятия\n"
            "6. Получение первых доходов"
        ),
        "next": "franchise_step_9"
    },
    "franchise_step_9": {
        "text": (
            "📚 <b>Обучение и поддержка:</b>\n\n"
            "• Онлайн-обучение и вебинары\n"
            "• Гайды и инструкции\n"
            "• Постоянная связь с куратором\n"
            "• Помощь в организации мероприятий\n"
            "• Регулярные обновления платформы"
        ),
        "next": "franchise_step_10"
    },
    "franchise_step_10": {
        "text": (
            "🗣 <b>Отзывы:</b>\n\n"
            "«Сотрудничество с Good Day стало отличным стартом в бизнесе. Поддержка на каждом этапе и понятная модель работы.»\n\n"
            "«Приложение востребовано в нашем городе. Пользователи довольны, бизнесы получают новых клиентов, а мы — стабильный доход.»"
        ),
        "next": "franchise_step_11"
    },
    "franchise_step_11": {
        "text": (
            "💵 <b>Стоимость франшизы:</b>\n\n"
            "<b>Тариф «Базовый»</b> — 200 000 рублей\n"
            "Роялти — 15%\n"
            "Льготный период: первые 6 месяцев — без роялти\n\n"
            "<b>Тариф «Стандарт»</b> — 300 000 рублей\n"
            "Роялти — 10%\n"
            "Первые 9 месяцев — без выплат по роялти\n\n"
            "<b>Тариф «Бизнес»</b> — 400 000 рублей\n"
            "Роялти — 5%\n"
            "Период без роялти — целый год\n\n"
            "<b>Тариф «Лайт»</b> — 100 000 рублей\n"
            "Доступен минимум для двух франчайзи в одном городе\n"
            "Для административных центров стартовая сумма увеличивается на 100 000 рублей\n\n"
            "<b>Окупаемость:</b> от 2 до 4 месяцев\n\n"
            "<b>Гарантия:</b>\n"
            "Мы уверены в надёжности франшизы и предоставляем гарантию возврата вложений.\n"
            "В случае непредвидённых обстоятельств с вашей стороны вы сможете вернуть средства."
        ),
        "next": None
    }
}

@router.callback_query(lambda c: c.data.startswith("franchise_step_"))
async def franchise_steps_handler(callback: types.CallbackQuery):
    step = callback.data
    content = franchise_steps.get(step)
    if content:
        buttons = []
        if content["next"]:
            buttons.append([InlineKeyboardButton(text="➡️ Далее", callback_data=content["next"])])
        buttons.append([InlineKeyboardButton(text="🔙 В меню", callback_data="back_to_menu")])
        await callback.message.edit_text(content["text"], parse_mode=ParseMode.HTML,
                                         reply_markup=InlineKeyboardMarkup(inline_keyboard=buttons))
    await callback.answer()

@router.callback_query(F.data == "back_to_menu")
async def back_to_menu(callback: types.CallbackQuery):
            await callback.message.edit_text(
                "📱 <b>Good Day</b> — это проект с различными направлениями и возможностями,\n"
                "но ключевым и объединяющим всё является наше <b>мобильное приложение</b>. 📲",
                parse_mode=ParseMode.HTML,
                reply_markup=main_menu
            )
            await callback.answer()
@router.callback_query(F.data == "download_presentation")
async def send_presentation(callback: types.CallbackQuery):
    try:
        file = FSInputFile("presentation.pdf")  # или "files/presentation.pdf" если в папке
        await callback.message.answer_document(file, caption="📄 Презентация франшизы Good Day")
    except Exception as e:
        await callback.message.answer("⚠️ Не удалось отправить презентацию. Убедитесь, что файл существует.")
        print(f"Ошибка: {e}")
    await callback.answer()

@router.callback_query(F.data == "watch_video")
async def send_video(callback: types.CallbackQuery):
    try:
        video = FSInputFile("intro.mp4")  # или "files/video.mp4"
        await callback.message.answer_video(video, caption="🎥 Видео-презентация Good Day")
    except Exception as e:
        await callback.message.answer("⚠️ Не удалось отправить видео. Убедитесь, что файл существует.")
        print(f"Ошибка: {e}")
    await callback.answer()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    keep_alive()  # запускаем веб-сервер для удержания Replit "живым"
    asyncio.run(main())  # запускаем бота



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
    await callback.message.answer("✅ Заявка отправлена! Мы свяжемся с Вами в ближайшее время.", reply_markup=main_menu)
    await callback.answer()

keep_alive()


if __name__ == "__main__":
    asyncio.run(main())
