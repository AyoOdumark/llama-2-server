from enum import Enum
from pydantic import BaseModel, constr
from datetime import datetime


class RoleEnum(str, Enum):
    system = "system"
    assistant = "assistant"
    user = "user"


class Query(BaseModel):
    message: str


class DbChatItem(BaseModel):
    session_id: str
    date: datetime
    message: str
    role: RoleEnum
