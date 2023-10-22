import os

from dotenv import load_dotenv

load_dotenv(
    "./.env",
    verbose=True,
)

BOT_TOKEN = os.environ.get("DISCORD_TOKEN")
