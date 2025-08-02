from datetime import datetime
from uuid import UUID, uuid4

from email_validator import EmailNotValidError, validate_email
from pydantic import EmailStr, field_validator
from sqlmodel import Field, SQLModel

from .enums.role import Role


class User(SQLModel, table=True, table_name="users"):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    first_name: str
    surname: str
    email: EmailStr = Field(unique=True)
    password: str = Field(unique=True)
    signature: bytes
    last_activity: datetime
    role: Role = Field(default=Role.USER)

    @field_validator("email", mode="before")
    @classmethod
    def validate_email_address(cls, value: str) -> str:
        try:
            valid = validate_email(value)
            return valid.email.lower()
        except EmailNotValidError as e:
            raise ValueError(f"Invalid email address: {e}")
