"""
Система активности в чате для Discord бота
Поддерживает активность в канале через автоматические сообщения, реакции и ответы
"""

import discord
from discord.ext import commands, tasks
import logging
import asyncio
import random
from datetime import datetime, timedelta

logger = logging.getLogger('chat_activity')

# ID канала для поддержки активности
ACTIVITY_CHANNEL_ID = 1375820312155000873  # Основной чат канал

# Время бездействия после которого бот начинает общаться (в минутах)
INACTIVITY_TIMEOUT = 30  

# Сообщения для поддержания активности
ACTIVITY_MESSAGES = [
    "Как дела, народ? 🤗",
    "Кто-нибудь онлайн? Давайте поболтаем!",
    "Что нового происходит? 💬",
    "Как настроение сегодня у всех?",
    "Есть планы на игру? 🎮",
    "Кто во что играет сейчас?",
    "Хорошего всем дня! ☀️",
    "Как проходит день? Делитесь новостями!",
    "Тихо тут стало... Все заняты? 😅",
    "Давайте немного поболтаем! Как дела у всех?",
    "Кто сегодня был в игре? Как успехи?",
    "Что интересного происходит в мире?",
    "Есть желающие пообщаться? 😊",
    "Как проходит ваш день, друзья?",
    "Что планируете на вечер? 🌙"
]

# Ответы на сообщения пользователей
RESPONSE_MESSAGES = [
    "Согласен! 👍",
    "Интересно!",
    "Хорошая мысль!",
    "Да, точно!",
    "Понятно 😊",
    "Круто!",
    "Отлично!",
    "Хм, интересно...",
    "Да, я тоже так думаю",
    "Супер! 🔥",
    "Классно!",
    "Понимаю тебя",
    "Хорошо сказано!",
    "Молодец!",
    "Это здорово!"
]

# Эмодзи для реакций
REACTION_EMOJIS = ['👍', '😊', '🔥', '💪', '👌', '❤️', '😄', '🎉', '⭐', '✨', '💯', '👏']

class ChatActivitySystem:
    def __init__(self, bot):
        self.bot = bot
        self.last_activity = {}  # Отслеживание последней активности по каналам
        self.setup_activity_tasks()
    
    def setup_activity_tasks(self):
        """Настройка задач для поддержания активности"""
        self.check_activity.start()
        self.random_reactions.start()
    
    @tasks.loop(minutes=5)  # Проверяем каждые 5 минут
    async def check_activity(self):
        """Проверка активности и отправка сообщений при необходимости"""
        try:
            channel = self.bot.get_channel(ACTIVITY_CHANNEL_ID)
            if not channel:
                return
            
            # Получаем последнее сообщение в канале
            try:
                messages = [message async for message in channel.history(limit=1)]
                if not messages:
                    return
                
                last_message = messages[0]
                
                # Если последнее сообщение от бота, не отправляем новое
                if last_message.author == self.bot.user:
                    return
                
                # Проверяем время последнего сообщения
                time_since_last = datetime.now(last_message.created_at.tzinfo) - last_message.created_at
                
                # Если прошло больше времени бездействия, отправляем сообщение
                if time_since_last > timedelta(minutes=INACTIVITY_TIMEOUT):
                    message = random.choice(ACTIVITY_MESSAGES)
                    await channel.send(message)
                    logger.info(f'Отправлено сообщение активности в канал: {message}')
                    
            except Exception as e:
                logger.error(f'Ошибка при проверке истории сообщений: {e}')
                
        except Exception as e:
            logger.error(f'Ошибка в проверке активности: {e}')
    
    @tasks.loop(minutes=random.randint(10, 30))  # Случайные интервалы
    async def random_reactions(self):
        """Случайные реакции на сообщения"""
        try:
            channel = self.bot.get_channel(ACTIVITY_CHANNEL_ID)
            if not channel:
                return
            
            # Получаем последние несколько сообщений
            messages = []
            async for message in channel.history(limit=5):
                if message.author != self.bot.user and not message.reactions:
                    messages.append(message)
            
            if messages:
                # Выбираем случайное сообщение для реакции
                message = random.choice(messages)
                emoji = random.choice(REACTION_EMOJIS)
                
                # Добавляем реакцию с небольшой вероятностью
                if random.random() < 0.3:  # 30% шанс
                    await message.add_reaction(emoji)
                    logger.info(f'Добавлена реакция {emoji} к сообщению')
                    
        except Exception as e:
            logger.error(f'Ошибка при добавлении реакций: {e}')
    
    async def respond_to_message(self, message):
        """Ответ на сообщение пользователя"""
        try:
            # Проверяем канал
            if message.channel.id != ACTIVITY_CHANNEL_ID:
                return
            
            # Не отвечаем на свои сообщения
            if message.author == self.bot.user:
                return
            
            # Не отвечаем на команды
            if message.content.startswith('!'):
                return
            
            # Случайный шанс ответить (15%)
            if random.random() < 0.15:
                response = random.choice(RESPONSE_MESSAGES)
                
                # Добавляем небольшую задержку для естественности
                await asyncio.sleep(random.randint(2, 8))
                await message.reply(response)
                logger.info(f'Ответ на сообщение: {response}')
            
            # Случайный шанс добавить реакцию (25%)
            elif random.random() < 0.25:
                emoji = random.choice(REACTION_EMOJIS)
                await message.add_reaction(emoji)
                logger.info(f'Добавлена реакция {emoji}')
                
        except Exception as e:
            logger.error(f'Ошибка при ответе на сообщение: {e}')
    
    @check_activity.before_loop
    async def before_check_activity(self):
        """Ожидание готовности бота"""
        await self.bot.wait_until_ready()
    
    @random_reactions.before_loop
    async def before_random_reactions(self):
        """Ожидание готовности бота"""
        await self.bot.wait_until_ready()
        # Добавляем случайную задержку при запуске
        await asyncio.sleep(random.randint(60, 300))  # 1-5 минут

async def setup_chat_activity(bot):
    """Настройка системы активности в чате"""
    try:
        # Создаем систему активности
        activity_system = ChatActivitySystem(bot)
        
        # Сохраняем ссылку на систему активности в боте
        bot.activity_system = activity_system
        
        # Находим канал и отправляем уведомление
        channel = bot.get_channel(ACTIVITY_CHANNEL_ID)
        if channel:
            logger.info(f'Система активности настроена для канала: {channel.name}')
        else:
            logger.error(f'Канал активности не найден с ID: {ACTIVITY_CHANNEL_ID}')
            
    except Exception as e:
        logger.error(f'Ошибка настройки системы активности: {e}')
        raise