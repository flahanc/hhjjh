# Discord Welcome Bot - Replit Configuration

## Overview

This is a Discord Welcome Bot designed specifically for the Limonericx server. The bot automatically sends welcome messages when new members join and goodbye messages when members leave the server. It's built using Python 3.11 and the discord.py library, with a simple modular architecture that separates configuration, bot logic, and main execution.

## System Architecture

### Backend Architecture
- **Language**: Python 3.11
- **Framework**: discord.py 2.5.2+ for Discord API integration
- **Architecture Pattern**: Object-oriented with event-driven programming
- **Deployment**: Single-process application with async/await patterns

### Key Design Decisions
- **Modular Configuration**: All server-specific settings are centralized in `config.py` for easy maintenance
- **Event-Driven Architecture**: Uses Discord.py's event system for handling member join/leave events
- **Async/Await Pattern**: Leverages Python's asyncio for non-blocking operations
- **Logging Integration**: Comprehensive logging to both file and console for debugging and monitoring

## Key Components

### Core Files
1. **`main.py`** - Application entry point with error handling and logging setup
2. **`bot.py`** - Main bot class containing Discord client logic and event handlers
3. **`config.py`** - Centralized configuration with environment variable support
4. **`.replit`** - Replit-specific configuration for running the bot

### Bot Functionality
- **Member Join Events**: Sends formatted welcome messages to designated channel
- **Member Leave Events**: Sends goodbye messages when users leave
- **Required Permissions**: Members intent, message content access, and guild events
- **Command Prefix**: Configurable command prefix (currently "!")

## Data Flow

1. **Bot Initialization**: 
   - Load configuration from environment variables
   - Set up Discord intents (members, message_content, guilds)
   - Initialize bot client with command prefix

2. **Event Processing**:
   - Monitor for member join/leave events
   - Format messages using templates from config
   - Send messages to designated welcome channel

3. **Error Handling**:
   - Comprehensive logging for debugging
   - Graceful shutdown on interruption
   - Exception handling for Discord API errors

## External Dependencies

### Discord Integration
- **discord.py**: Primary library for Discord API interaction
- **Bot Token**: Stored in environment variable `DISCORD_TOKEN`
- **Server Configuration**: Hard-coded server and channel IDs for Limonericx server

### Python Dependencies
- **asyncio**: For asynchronous programming
- **logging**: For application monitoring and debugging
- **os**: For environment variable access

## Deployment Strategy

### Replit Configuration
- **Runtime**: Python 3.11 with Nix package manager
- **Startup Command**: Automatic pip install of discord.py followed by bot execution
- **Parallel Workflows**: Configured for easy project management within Replit

### Environment Requirements
- **DISCORD_TOKEN**: Must be set as environment variable (fallback token present in config)
- **Network Access**: Requires outbound HTTPS for Discord API communication
- **Persistent Storage**: Bot logs are written to `bot.log` file

### Deployment Commands
```bash
pip install discord.py && python main.py
```

## Changelog
- June 23, 2025: Initial setup with Russian welcome/goodbye messages
- June 23, 2025: Added bot token and configured for Limonericx server
- June 23, 2025: Created backup simple bot version for manual commands
- June 23, 2025: Enhanced messages with Discord embeds, green sidebar for welcome, orange for goodbye
- June 23, 2025: Added clickable links and buttons to welcome messages for better user experience
- June 23, 2025: Updated welcome links to correct channel (1375772176107700266)
- June 23, 2025: Removed broken link, disabled button until correct URL provided
- June 23, 2025: Re-enabled links - they work for server members after joining
- June 23, 2025: Added complete ticket support system with forms, categories, and moderation tools
- June 23, 2025: Updated ticket system to create private channels with role-based access control
- June 23, 2025: Added admin application systems for both Minecraft and Discord with forms and review workflow
- June 23, 2025: Added chat activity system with automatic messaging, emoji reactions, and replies to maintain server engagement

## Current Status
- ✅ Bot is running successfully and connected to Limonericx server
- ✅ Successfully sending Russian welcome/goodbye messages  
- ✅ Fixed duplicate message issue by removing extra workflow
- ✅ Bot targets specific channel: 1385303735281914011 (⛈️・qq-bb)
- ✅ Privileged intents are working correctly

## User Preferences

Preferred communication style: Simple, everyday language.
Language: Russian messages for Discord bot functionality.