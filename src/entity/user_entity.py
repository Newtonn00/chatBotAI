from dataclasses import dataclass, asdict


@dataclass
class UserEntity:
    id: int
    username: str

    def as_dict(self) -> dict:
        return asdict(self)



