from typing import Any

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
