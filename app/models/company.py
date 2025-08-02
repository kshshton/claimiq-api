from typing import Optional
from uuid import UUID, uuid4

from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class Company(SQLModel, table=True, table_name="companies"):
    id: UUID = Field(default_factory=uuid4, primary_key=True)
    logo: Optional[bytes] = None
    company_name: str
    street: str
    postal_code: str
    town: str
    nip: str = Field(unique=True)
    email: Optional[EmailStr] = Field(default=None, max_length=320)
    phone_number: Optional[str] = Field(default=None, max_length=12)
    branch_name: Optional[str] = None
    branch_address: Optional[str] = None
