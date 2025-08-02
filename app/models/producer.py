from sqlmodel import Field, SQLModel


class Producer(SQLModel, table=True, table_name="producers"):
    name: str = Field(primary_key=True)
