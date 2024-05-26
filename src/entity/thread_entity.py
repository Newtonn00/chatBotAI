from dataclasses import dataclass, asdict


@dataclass
class ThreadEntity:
    id: int
    thread_id: str
    user_id: int
    created_on_timestamp: int
    content: str
    active: bool

    def as_dict(self) -> dict:
        return asdict(self)



