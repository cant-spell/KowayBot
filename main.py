import discord

from src import KowayBot, BOT_TOKEN

bot = KowayBot(
    commands_prefix=">>>",
    intents=discord.Intents.all()
)

bot.run(BOT_TOKEN)
