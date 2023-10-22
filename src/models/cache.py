import datetime
from typing import Any, Union

from dataclasses import dataclass, field


@dataclass(repr=True)
class Cache:
    storage: dict[int, Any] = field(default_factory=dict)
    
    def get_key(self, key: int):
        return self.storage.get(key)
    
    def insert_key(self, key: int, value: Any):
        self.storage[key] = value
        
    def __len__(self):
        return len(self.storage)


@dataclass(repr=True)
class MemberCache:
    ids: list[int] = field(default_factory=list)
    dt_join: list[datetime.datetime] = field(default_factory=list)
    dt_creation: list[datetime.datetime] = field(default_factory=list)

    def put_id(self, _id: int) -> None:
        self.ids.append(_id)

    def get_ids(self) -> list[int]:
        return self.ids

    @staticmethod
    def get_rough_join_time(
            curr_time: datetime.datetime,
            copied_dataset: list[datetime]
    ) -> int:
        """
        Function to get a rough time of accounts joining
        """
        copy = copied_dataset
        total_seconds = 0
        for i in copy:
            total_seconds += (curr_time - i).total_seconds()
        return total_seconds // len(copy)

    @staticmethod
    def get_rough_creation_time(
            curr_time: datetime.datetime,
            copied_dataset: list[datetime.datetime]
    ) -> int:
        """
        Function to get a rough time for the account creation dates
        """
        copy = copied_dataset
        total_seconds = 0
        for i in copy:
            total_seconds += (curr_time - i).days
        return total_seconds // len(copy)

    def gather_info(self) -> list[list[int], int, int]:
        """
        Function to aggregate all information as a list
        """
        curr = datetime.datetime.utcnow()
        id_ds, dt_ds, ct_ds = self.ids.copy(), self.dt_join.copy(), self.dt_creation.copy()
        avg_join_time = self.get_rough_join_time(curr, dt_ds)
        avg_creation_time = self.get_rough_creation_time(curr, ct_ds)

        return [
            id_ds,
            avg_join_time,
            avg_creation_time
        ]


class GuildCache:
    guilds: dict[int, dict[str, Union[MemberCache, Cache]]] = field(default_factory=dict)

    def get_guild(self, _id: int):
        return self.guilds.get(_id)

    def put_guild(self, _id: int):
        self.guilds[_id] = {}
