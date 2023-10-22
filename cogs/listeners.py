from typing import TYPE_CHECKING

import discord
from discord.ext import commands

if TYPE_CHECKING:
    from src.models.bot import KowayBot


class ListenerManCog(
    commands.Cog, command_attrs=dict(hidden=True)
):
    def __init__(self, bot: KowayBot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if member.guild.id in self.bot.guild_cache:
            gcache = self.bot.guild_cache.get_guild(member.guild.id)
            member_cache = gcache['member']
            member_cache.insert_key(member.guild.id)
            member_cache.put_dt_join_time(member.joined_at)
            member_cache.put_dt_creation_time(member.created_at)
        
        