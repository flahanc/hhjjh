"""
Discord Welcome Bot Implementation
Handles member join/leave events and sends appropriate messages
"""

import discord
from discord.ext import commands
import logging
import asyncio
from support_system import setup_support_system
from admin_applications import setup_minecraft_admin_applications, setup_discord_admin_applications
from chat_activity import setup_chat_activity
from config import (
    DISCORD_TOKEN,
    LIMONERICX_SERVER_ID,
    WELCOME_CHANNEL_ID,
    WELCOME_COLOR,
    GOODBYE_COLOR,
    WELCOME_TITLE,
    WELCOME_DESCRIPTION,
    WELCOME_FIELDS,
    GOODBYE_TITLE,
    GOODBYE_DESCRIPTION,
    WELCOME_BUTTON_ENABLED,
    WELCOME_BUTTON_LABEL,
    WELCOME_BUTTON_URL,
    BOT_COMMAND_PREFIX,
    BOT_ACTIVITY_NAME
)

logger = logging.getLogger(__name__)

class DiscordWelcomeBot:
    """Discord bot class for handling welcome and goodbye messages"""
    
    def __init__(self):
        """Initialize the Discord bot with required intents"""
        # Set up bot intents
        intents = discord.Intents.default()
        intents.members = True  # Required for member join/leave events
        intents.message_content = True  # Required for message content access
        intents.guilds = True  # Required for guild events
        
        # Initialize bot
        self.bot = commands.Bot(
            command_prefix=BOT_COMMAND_PREFIX,
            intents=intents,
            help_command=None
        )
        
        # Set up event handlers
        self._setup_events()
    
    def _setup_events(self):
        """Set up bot event handlers"""
        
        @self.bot.event
        async def on_ready():
            """Event triggered when bot is ready and connected"""
            logger.info(f'{self.bot.user} подключился к Discord!')
            logger.info(f'Bot ID: {self.bot.user.id}')
            
            # Set bot activity status
            activity = discord.Game(name=BOT_ACTIVITY_NAME)
            await self.bot.change_presence(activity=activity)
            
            # Log server information
            guild = self.bot.get_guild(LIMONERICX_SERVER_ID)
            if guild:
                logger.info(f'Подключен к серверу: {guild.name} (ID: {guild.id})')
                logger.info(f'Количество участников: {guild.member_count}')
            else:
                logger.warning(f'Не удалось найти сервер с ID: {LIMONERICX_SERVER_ID}')
            
            # Check if welcome channel exists
            channel = self.bot.get_channel(WELCOME_CHANNEL_ID)
            if channel:
                logger.info(f'Канал приветствия найден: {channel.name} (ID: {channel.id})')
            else:
                logger.error(f'Канал приветствия не найден с ID: {WELCOME_CHANNEL_ID}')
            
            # Setup support ticket system
            try:
                await setup_support_system(self.bot)
                logger.info('Система тикетов технической поддержки настроена')
            except Exception as e:
                logger.error(f'Ошибка настройки системы поддержки: {e}')
            
            # Setup admin application systems
            try:
                await setup_minecraft_admin_applications(self.bot)
                logger.info('Система заявок в администрацию Minecraft настроена')
            except Exception as e:
                logger.error(f'Ошибка настройки системы заявок в администрацию Minecraft: {e}')
            
            try:
                await setup_discord_admin_applications(self.bot)
                logger.info('Система заявок в администрацию Discord настроена')
            except Exception as e:
                logger.error(f'Ошибка настройки системы заявок в администрацию Discord: {e}')
            
            # Setup chat activity system
            try:
                await setup_chat_activity(self.bot)
                logger.info('Система активности в чате настроена')
            except Exception as e:
                logger.error(f'Ошибка настройки системы активности в чате: {e}')
        
        @self.bot.event
        async def on_message(message):
            """Event triggered when a message is sent"""
            # Обрабатываем сообщения через систему активности
            if hasattr(self.bot, 'activity_system'):
                await self.bot.activity_system.respond_to_message(message)
            
            # Обрабатываем команды
            await self.bot.process_commands(message)

        @self.bot.event
        async def on_member_join(member):
            """Event triggered when a member joins the server"""
            try:
                # Check if the member joined the correct server
                if member.guild.id != LIMONERICX_SERVER_ID:
                    return
                
                logger.info(f'Новый участник присоединился: {member.name} (ID: {member.id})')
                
                # Get the welcome channel
                channel = self.bot.get_channel(WELCOME_CHANNEL_ID)
                if not channel:
                    logger.error(f'Канал приветствия не найден: {WELCOME_CHANNEL_ID}')
                    return
                
                # Create beautiful welcome embed with green sidebar
                embed = discord.Embed(
                    title=WELCOME_TITLE,
                    description=f"{WELCOME_DESCRIPTION}\n\n{member.mention}",
                    color=WELCOME_COLOR
                )
                
                # Add fields with information
                for field in WELCOME_FIELDS:
                    embed.add_field(
                        name=field["name"],
                        value=field["value"],
                        inline=field["inline"]
                    )
                
                # Add user avatar as thumbnail
                embed.set_thumbnail(url=member.display_avatar.url)
                
                # Add footer with server info
                embed.set_footer(
                    text=f"Участник #{member.guild.member_count} • Добро пожаловать!",
                    icon_url=member.guild.icon.url if member.guild.icon else None
                )
                
                # Send embed message (with button only if enabled and URL provided)
                if WELCOME_BUTTON_ENABLED and WELCOME_BUTTON_URL:
                    view = discord.ui.View(timeout=None)
                    button = discord.ui.Button(
                        label=WELCOME_BUTTON_LABEL,
                        url=WELCOME_BUTTON_URL,
                        style=discord.ButtonStyle.link
                    )
                    view.add_item(button)
                    await channel.send(embed=embed, view=view)
                else:
                    await channel.send(embed=embed)
                
                logger.info(f'Отправлено приветствие для {member.name}')
                
            except discord.Forbidden as e:
                logger.error(f'Нет разрешения для отправки сообщения: {e}')
            except discord.HTTPException as e:
                logger.error(f'Ошибка HTTP при отправке приветствия: {e}')
            except Exception as e:
                logger.error(f'Неожиданная ошибка при приветствии: {e}')
        
        @self.bot.event
        async def on_member_remove(member):
            """Event triggered when a member leaves the server"""
            try:
                # Check if the member left the correct server
                if member.guild.id != LIMONERICX_SERVER_ID:
                    return
                
                logger.info(f'Участник покинул сервер: {member.name} (ID: {member.id})')
                
                # Get the welcome channel
                channel = self.bot.get_channel(WELCOME_CHANNEL_ID)
                if not channel:
                    logger.error(f'Канал приветствия не найден: {WELCOME_CHANNEL_ID}')
                    return
                
                # Create beautiful goodbye embed with orange sidebar
                embed = discord.Embed(
                    title=GOODBYE_TITLE,
                    description=f"{member.mention}\n\n{GOODBYE_DESCRIPTION}",
                    color=GOODBYE_COLOR
                )
                
                # Add user avatar as thumbnail
                embed.set_thumbnail(url=member.display_avatar.url)
                
                # Add footer with server info
                embed.set_footer(
                    text=f"До свидания! • Участников осталось: {member.guild.member_count}",
                    icon_url=member.guild.icon.url if member.guild.icon else None
                )
                
                # Send beautiful embed message
                await channel.send(embed=embed)
                logger.info(f'Отправлено прощание для {member.name}')
                
            except discord.Forbidden as e:
                logger.error(f'Нет разрешения для отправки сообщения: {e}')
            except discord.HTTPException as e:
                logger.error(f'Ошибка HTTP при отправке прощания: {e}')
            except Exception as e:
                logger.error(f'Неожиданная ошибка при прощании: {e}')
        
        @self.bot.event
        async def on_error(event, *args, **kwargs):
            """Global error handler for bot events"""
            logger.error(f'Ошибка в событии {event}: {args}')
        
        @self.bot.event
        async def on_command_error(ctx, error):
            """Handle command errors"""
            if isinstance(error, commands.CommandNotFound):
                return  # Ignore unknown commands
            
            logger.error(f'Ошибка команды в {ctx.channel}: {error}')
            
            try:
                await ctx.send(f'Произошла ошибка: {str(error)}')
            except discord.HTTPException:
                logger.error('Не удалось отправить сообщение об ошибке')
    
    async def start_bot(self):
        """Start the Discord bot"""
        try:
            logger.info('Запуск Discord бота...')
            
            # Validate token
            if not DISCORD_TOKEN:
                raise ValueError('Discord токен не найден в переменных окружения или конфигурации')
            
            # Start the bot
            await self.bot.start(DISCORD_TOKEN)
            
        except discord.LoginFailure:
            logger.error('Неверный Discord токен')
            raise
        except discord.HTTPException as e:
            logger.error(f'HTTP ошибка при подключении: {e}')
            raise
        except Exception as e:
            logger.error(f'Неожиданная ошибка при запуске бота: {e}')
            raise
        finally:
            if not self.bot.is_closed():
                await self.bot.close()
                logger.info('Бот отключен')
    
    def add_command(self, command):
        """Add a custom command to the bot"""
        self.bot.add_command(command)
    
    async def stop_bot(self):
        """Gracefully stop the bot"""
        logger.info('Остановка бота...')
        if not self.bot.is_closed():
            await self.bot.close()
