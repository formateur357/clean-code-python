from dataclasses import dataclass
from typing import Optional

@dataclass
class User:
    email: str
    is_active: bool
    reset_token: Optional[str] = None