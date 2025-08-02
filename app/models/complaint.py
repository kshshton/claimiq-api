from datetime import date
from typing import Optional
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel

from .enums.complaint_type import ComplaintType


class Complaint(SQLModel, table=True, table_name="complaints"):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    number: str = Field(unique=True)
    type: ComplaintType
    submit_date: date = Field(default_factory=date.today)
    exit_date: Optional[date] = None
    status: str
