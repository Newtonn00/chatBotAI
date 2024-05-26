from dataclasses import dataclass, asdict


@dataclass
class MessageEntity:
    id: int
    user_id: int
    thread_id: str
    message_timestamp: int
    role: str
    message_text: str

    def as_dict(self) -> dict:
        return asdict(self)