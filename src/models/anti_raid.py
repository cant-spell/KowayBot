from __future__ import annotations
from typing import TYPE_CHECKING
from enum import Enum

from .cache import MemberCache

if TYPE_CHECKING:
    from .bot import KowayBot


class ActionType(Enum):
    Alert = 0
    Kick = 1
    Ban = 2


class AntiRaid:
    def __init__(self, bot: KowayBot):
        self.bot = bot
        self.member_cache = MemberCache()

        self.protected_servers: dict[
            int,
            list[
                bool, ActionType
            ]
        ] = {}
        self.under_raid_servers: list[int, ...] = []

    def determine_raid(self):
        self.member_cache.gather_info()
