"""
Упрощенная версия Discord бота без привилегированных прав
Работает через команды вместо автоматических событий
"""

import discord
from discord.ext import commands
import logging
from typing import Optional
from config import (
    DISCORD_TOKEN,
    LIMONERICX_SERVER_ID,
    WELCOME_CHANNEL_ID,
    WELCOME_MESSAGE_TEMPLATE,
    GOODBYE_MESSAGE_TEMPLATE,
    BOT_COMMAND_PREFIX,
    BOT_ACTIVITY_NAME
)

logger = logging.getLogger(__name__)

class SimpleDiscordBot:
    """Упрощенная версия бота без привилегированных прав"""
    
    def __init__(self):
        """Инициализация бота с базовыми правами"""
        # Базовые права без privileged intents
        intents = discord.Intents.default()
        intents.message_content = False  # Отключаем для избежания проблем
        
        self.bot = commands.Bot(
            command_prefix=BOT_COMMAND_PREFIX,
            intents=intents,
            help_command=None
        )
        
        self._setup_events()
        self._setup_commands()
    
    def _setup_events(self):
        """Настройка базовых событий"""
        
        @self.bot.event
        async def on_ready():
            """Событие готовности бота"""
            logger.info(f'{self.bot.user} подключился к Discord!')
            
            # Устанавливаем активность
            activity = discord.Game(name=BOT_ACTIVITY_NAME)
            await self.bot.change_presence(activity=activity)
            
            # Проверяем сервер
            guild = self.bot.get_guild(LIMONERICX_SERVER_ID)
            if guild:
                logger.info(f'Подключен к серверу: {guild.name}')
            else:
                logger.warning(f'Сервер не найден: {LIMONERICX_SERVER_ID}')
    
    def _setup_commands(self):
        """Настройка команд бота"""
        
        @self.bot.command(name='welcome')
        async def welcome_command(ctx, user: discord.Member = None):
            """Команда приветствия участника"""
            if ctx.channel.id != WELCOME_CHANNEL_ID:
                return
            
            target_user = user if user else ctx.author
            
            welcome_message = WELCOME_MESSAGE_TEMPLATE.format(
                user_mention=target_user.mention
            )
            
            await ctx.send(welcome_message)
            logger.info(f'Отправлено приветствие для {target_user.name}')
        
        @self.bot.command(name='goodbye')
        async def goodbye_command(ctx, *, username: Optional[str] = None):
            """Команда прощания с участником"""
            if ctx.channel.id != WELCOME_CHANNEL_ID:
                return
            
            display_name = username if username else ctx.author.display_name
            
            goodbye_message = GOODBYE_MESSAGE_TEMPLATE.format(
                user_mention=f"**{display_name}**"
            )
            
            await ctx.send(goodbye_message)
            logger.info(f'Отправлено прощание для {display_name}')
        
        @self.bot.command(name='info')
        async def info_command(ctx):
            """Информация о боте"""
            if ctx.channel.id != WELCOME_CHANNEL_ID:
                return
            
            embed = discord.Embed(
                title="Discord Bot для Limonericx",
                description="Бот для приветствия участников",
                color=0x00ff00
            )
            embed.add_field(
                name="Команды",
                value="!welcome @пользователь - приветствие\n!goodbye имя - прощание",
                inline=False
            )
            
            await ctx.send(embed=embed)
    
    async def start_bot(self):
        """Запуск бота"""
        try:
            logger.info('Запуск упрощенного Discord бота...')
            
            if not DISCORD_TOKEN:
                raise ValueError('Discord токен не найден')
            
            await self.bot.start(DISCORD_TOKEN)
            
        except Exception as e:
            logger.error(f'Ошибка при запуске: {e}')
            raise
        finally:
            if not self.bot.is_closed():
                await self.bot.close()