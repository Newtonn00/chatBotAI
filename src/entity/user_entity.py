from dataclasses import dataclass, asdict


@dataclass
class UserEntity:
    id: str
    name: str

    def as_dict(self) -> dict:
        return asdict(self)



