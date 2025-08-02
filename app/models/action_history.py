from datetime import date as date_
from typing import Optional
from uuid import UUID, uuid4

from pydantic import EmailStr
from sqlmodel import Field, SQLModel

from .enums.action import Action


class ActionHistory(SQLModel, table=True, table_name="actions_history"):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    email: EmailStr = Field(foreign_key="users.email")
    action: Action
    date: date_ = Field(default_factory=date_.today)
    details: Optional[str] = None
