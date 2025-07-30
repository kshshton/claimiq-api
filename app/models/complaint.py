from datetime import date
from typing import Optional
from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class Complaint(SQLModel, table=True):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    complaint_number: str
    submit_date: date = Field(default_factory=date.today)
    exit_date: Optional[date]
    type: str
    status: str
    exit: bool = False
