from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command  # Добавьте этот импорт
from utils import create_keyboard

router = Router()

@router.message(Command("help"))  # Теперь Command импортирован
async def cmd_help(message: Message):
    help_text = (
        "🤖 **AttendanceTrackerBot**\n\n"
        "Этот бот помогает вести учет посещаемости учащихся и отправлять данные коллегам.\n\n"
        "📋 **Основные команды:**\n"
        "- /start: Начать работу с ботом.\n"
        "- /help: Получить справку о возможностях бота.\n\n"
        "🛠 **Что умеет бот:**\n"
        "1. **Добавление учащихся**: Введите ФИО ученика (например, Иванов Иван Иванович).\n"
        "2. **Отправка данных**: Укажите username получателя, и бот отправит ему данные после подтверждения.\n"
        "3. **Расписание**: Загрузите изображение с расписанием, и бот отправит его получателю.\n"
        "4. **Инлайн-режим**: Используйте @YourBotName в любом чате для быстрой отправки данных.\n\n"
        "📂 **Логирование**: Все сообщения сохраняются в файл `user_messages.txt`.\n\n"
        "📞 **Поддержка**: Если возникли вопросы, напишите @your_username."
    )

    await message.answer(
        help_text,
        reply_markup=create_keyboard(["Добавить", "Завершить", "Расписание", "/help"]),
        parse_mode="Markdown"
    )