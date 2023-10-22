import datetime
import os

import aiohttp
from discord import Message
from discord.ext import commands

from .cache import Cache
from .anti_raid import AntiRaid


class KowayBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.session: aiohttp.ClientSession = None  # type: ignore
        self.cache: Cache = None  # type: ignore
        
        self.message_count = 0
        
        self.start_time: datetime.datetime = None   # type: ignore
        self.anti_raid_system = AntiRaid(self)

    async def start(self, token: str, *, reconnect: bool = True):
        self.start_time = datetime.datetime.utcnow()
        self.cache = Cache()
        async with aiohttp.ClientSession() as self.session:
            return await super().start(token, reconnect=reconnect)
    
    async def on_message(self, message: Message, /) -> None:
        self.message_count += 1
        return await super().on_message(message)
    
    async def get_message_count(self):
        return self.message_count
    
    async def get_guild_count(self):
        return len(self.guilds)
    
    async def setup_hook(self) -> None:
        for file in os.listdir('./cogs'):
            if file.endswith(".py"):
                try:
                    await self.load_extension(f"cogs.{file[:-3]}")
                except Exception as e:
                    print(f"Couldn't Load cogs/{file}")
                    print(e)
    
    async def get_start_time(self):
        return self.start_time
    

        
        
