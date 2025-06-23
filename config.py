"""
Configuration settings for the Discord Welcome Bot
"""

import os

# Discord Bot Configuration
DISCORD_TOKEN = "MTM3NjU0ODM0NzA5NTI4NTg3Mg.G8o3TO.LhYCStHjRC-BSYXmHSw-mhloGIZlO3UflK3kWQ"

# Server and Channel Configuration
LIMONERICX_SERVER_ID = 1375772175373566012
WELCOME_CHANNEL_ID = 1385303735281914011
SUPPORT_CHANNEL_ID = 1375826419158089751
SUPPORT_ROLE_ID = 1376222106760773836  # Роль техподдержки
TICKETS_CATEGORY_ID = None  # Категория для тикетов (будет создана автоматически)

# Admin Application Channels
MINECRAFT_ADMIN_APPLICATION_CHANNEL_ID = 1375818535141376030  # Канал для подачи заявок в Minecraft администрацию
MINECRAFT_ADMIN_RESPONSES_CHANNEL_ID = 1375873913321689098    # Канал куда отправляются заявки в Minecraft администрацию
DISCORD_ADMIN_APPLICATION_CHANNEL_ID = 1375818773994537001    # Канал для подачи заявок в Discord администрацию
DISCORD_ADMIN_RESPONSES_CHANNEL_ID = 1375850180007563264      # Канал куда отправляются заявки в Discord администрацию

# Embed Colors (hex colors)
WELCOME_COLOR = 0x00ff00  # Зеленый цвет для приветствия
GOODBYE_COLOR = 0xff8c00   # Оранжевый цвет для прощания

# Message Templates for Embeds
WELCOME_TITLE = "🎉 Добро пожаловать на Limonericx!"
WELCOME_DESCRIPTION = "Рады видеть тебя в нашем сообществе!"

WELCOME_FIELDS = [
    {
        "name": "📚 Для новичков",
        "value": "У нас есть вся нужная информация — [нажми сюда](https://discord.com/channels/1375772175373566012/1375772176107700266), чтобы узнать больше!",
        "inline": False
    },
    {
        "name": "❓ Нужна помощь?",
        "value": "Если что-то будет непонятно — не стесняйся задавать вопросы, мы всегда поможем!",
        "inline": False
    }
]

# Welcome button configuration
WELCOME_BUTTON_ENABLED = True
WELCOME_BUTTON_LABEL = "📖 Информация для новичков"
WELCOME_BUTTON_URL = "https://discord.com/channels/1375772175373566012/1375772176107700266"

GOODBYE_TITLE = "👋 Пользователь покинул сервер"
GOODBYE_DESCRIPTION = "Жаль, что ты ушёл! Надеемся увидеть тебя снова."

# Support Ticket Configuration
SUPPORT_EMBED_COLOR = 0x0099ff  # Синий цвет для тех поддержки
SUPPORT_TITLE = "🛠️ Техническая поддержка Limonericx"
SUPPORT_DESCRIPTION = "Нужна помощь с сервером Minecraft? Создайте тикет и мы поможем!"

SUPPORT_FIELDS = [
    {
        "name": "📋 Как создать тикет:",
        "value": "1️⃣ Нажмите кнопку **Создать тикет**\n2️⃣ Укажите ваш ник в Minecraft\n3️⃣ Опишите проблему подробно\n4️⃣ Ожидайте ответа модераторов",
        "inline": False
    },
    {
        "name": "⚡ Что указывать:",
        "value": "• Точный ник на сервере\n• Время когда произошла проблема\n• Подробное описание ситуации\n• Скриншоты (если есть)",
        "inline": True
    },
    {
        "name": "⏰ Время ответа:",
        "value": "• Обычно: 1-6 часов\n• В выходные: до 24 часов\n• Срочные вопросы решаются быстрее",
        "inline": True
    }
]

SUPPORT_BUTTON_LABEL = "🎫 Создать тикет"

# Ticket Categories
TICKET_CATEGORIES = [
    {"label": "🐛 Баг/Ошибка", "value": "bug", "emoji": "🐛"},
    {"label": "💰 Проблемы с экономикой", "value": "economy", "emoji": "💰"},
    {"label": "🏠 Проблемы с регионами", "value": "regions", "emoji": "🏠"},
    {"label": "👥 Жалоба на игрока", "value": "player_report", "emoji": "👥"},
    {"label": "❓ Другое", "value": "other", "emoji": "❓"}
]

# Minecraft Admin Application Configuration
MINECRAFT_ADMIN_EMBED_COLOR = 0x00ff00  # Зеленый цвет для заявок в администрацию
MINECRAFT_ADMIN_TITLE = "🛡️ Заявка в администрацию Minecraft сервера"
MINECRAFT_ADMIN_DESCRIPTION = "Хотите стать частью команды администраторов? Заполните заявку!"

MINECRAFT_ADMIN_FIELDS = [
    {
        "name": "📋 Что нужно для заявки:",
        "value": "1️⃣ Ваш точный игровой ник\n2️⃣ Причина почему вас должны взять\n3️⃣ Ваш возраст\n4️⃣ Опыт администрирования",
        "inline": False
    },
    {
        "name": "⚡ Требования:",
        "value": "• Возраст от 16 лет\n• Опыт игры на сервере\n• Активность в Discord\n• Адекватность и стрессоустойчивость",
        "inline": True
    },
    {
        "name": "⏰ Рассмотрение:",
        "value": "• Обычно: 3-7 дней\n• Собеседование при одобрении\n• Результат сообщат в ЛС",
        "inline": True
    }
]

MINECRAFT_ADMIN_BUTTON_LABEL = "📝 Подать заявку"

# Discord Admin Application Configuration
DISCORD_ADMIN_EMBED_COLOR = 0x5865f2  # Discord цвет для заявок в Discord администрацию
DISCORD_ADMIN_TITLE = "🎫 Заявка в администрацию Discord сервера"
DISCORD_ADMIN_DESCRIPTION = "Хотите модерировать наш Discord? Подайте заявку!"

DISCORD_ADMIN_FIELDS = [
    {
        "name": "📋 Что нужно для заявки:",
        "value": "1️⃣ Ваш ник в Discord\n2️⃣ Причина почему вас должны взять\n3️⃣ Ваш возраст\n4️⃣ Опыт модерирования Discord",
        "inline": False
    },
    {
        "name": "⚡ Требования:",
        "value": "• Возраст от 15 лет\n• Активность в Discord\n• Знание правил сервера\n• Опыт работы с Discord ботами",
        "inline": True
    },
    {
        "name": "⏰ Рассмотрение:",
        "value": "• Обычно: 2-5 дней\n• Тестовое задание при одобрении\n• Результат сообщат в ЛС",
        "inline": True
    }
]

DISCORD_ADMIN_BUTTON_LABEL = "📝 Подать заявку"

# Bot Settings
BOT_COMMAND_PREFIX = "!"
BOT_ACTIVITY_NAME = "Добро пожаловать на Limonericx!"
