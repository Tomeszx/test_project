from dataclasses import dataclass


@dataclass
class Cookie:
    domain: str
    httpOnly: bool
    name: str
    path: str
    sameSite: str
    secure: bool
    value: str
    expiry: str | None = None
