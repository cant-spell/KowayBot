from typing import TYPE_CHECKING

from discord.ext import commands, tasks

if TYPE_CHECKING:
    from src.models.bot import KowayBot


class TaskManCog(
    commands.Cog, command_attrs=dict(hidden=True)
):
    def __init__(self, bot: KowayBot):
        self.bot = bot

    async def cog_load(self) -> None:
        self.anti_raid_task.start()

    @tasks.loop(seconds=10)
    async def anti_raid_task(self):
        # TODO: need to finish this logic
        ...

    @anti_raid_task.before_loop
    async def before_anti_raid_task(self):
        await self.bot.wait_until_ready()


async def setup(bot: KowayBot):
    await bot.add_cog(TaskManCog(bot))
