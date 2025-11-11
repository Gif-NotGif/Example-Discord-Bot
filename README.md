# Sample Discord Bot

A bare bones Discord bot that responds to the `/test` slash command with "Hello World!".

## Prerequisites

- Python 3.8 or higher
- A Discord account

## Setup

### 1. Create a Virtual Environment

Create and activate a virtual environment to isolate dependencies:

**Windows (PowerShell):**
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
python -m venv venv
venv\Scripts\activate.bat
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Create a Discord Bot Application

Follow the official Discord documentation to create a bot and get your token:

**Creating a Bot Account:**
- [Discord Developer Portal - Getting Started](https://discord.com/developers/docs/getting-started)
- [Discord Developer Portal - Creating a Bot Account](https://discord.com/developers/docs/topics/oauth2#bots)

**Quick Steps:**
1. Go to the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" and give it a name
3. Go to the "Bot" section in the left sidebar
4. Under the TOKEN section, click "Reset Token" and copy your bot token

> [!WARNING]
> Important: Keep this token secret!

**Inviting the Bot to Your Server:**
1. Go to the "OAuth2" > "URL Generator" section
2. Under SCOPES, select:
   - `bot`
   - `applications.commands`
3. Under BOT PERMISSIONS, select:
   - `Send Messages`
   - `Use Slash Commands`
4. Copy the generated URL at the bottom and open it in your browser
5. Select the server you want to add the bot to and authorize

For more details, see the [Discord.py Documentation - Creating a Bot Account](https://discordpy.readthedocs.io/en/stable/discord.html).

### 4. Configure Environment Variables

Create a `.env` file from the example:

```bash
copy .env.example .env
```

Edit the `.env` file and add your bot token:

```
DISCORD_TOKEN=your_actual_token_here
```

### 5. Run the Bot

```bash
python bot.py
```

> [!TIP]
> This will only run the bot locally. If you close the process running the bot or shut down your computer, then the bot will go offline. If you want the bot to be up 100% of the time, consider hosting the bot on a server.

You should see output indicating the bot has logged in successfully.

## Usage

Once the bot is running and added to your server, use the `/test` command in any channel to receive a "Hello World!" message.

## Deactivating the Virtual Environment

When you're done working with the bot, deactivate the virtual environment:

```bash
deactivate
```
