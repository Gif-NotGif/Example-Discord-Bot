import discord
from discord import app_commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create bot instance
intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    """Called when the bot is ready"""
    await tree.sync()
    print(f'Logged in as {client.user}')
    print('Bot is ready!')

@tree.command(name="test", description="Test command that sends Hello World")
async def test_command(interaction: discord.Interaction):
    """Responds with Hello World message"""
    await interaction.response.send_message("Hello World!")

# Run the bot
if __name__ == "__main__":
    token = os.getenv('DISCORD_TOKEN')
    if not token:
        print("Error: DISCORD_TOKEN environment variable not set")
        exit(1)
    client.run(token)
