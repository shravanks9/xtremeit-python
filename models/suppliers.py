
from datetime import datetime
from typing import Optional

from sqlmodel import Column, Field, SQLModel, TIMESTAMP, text, Date,DateTime

from lib.database import engine


# Define the SQLModel configuration object
class Config:
    arbitrary_types_allowed = True
    ...


class SupplierSkeleton(SQLModel):

    contactfname: Optional[str] = Field(max_length=50, nullable=False)

    contactlname: Optional[str] = Field(max_length=50, nullable=True)

    username: Optional[str] = Field(max_length=100, nullable=False,unique=True)

    password: Optional[str] = Field(max_length=100, nullable=False)

    email: Optional[str] = Field(max_length=100, nullable=True,unique=True)



class SupplierBase(SupplierSkeleton):

    company_name: Optional[str] = Field(max_length=1024, nullable=True)

    address: Optional[str] = Field(max_length=500, nullable=True)

    phone_number: Optional[str] = Field(max_length=45, nullable=True)

    country: Optional[str] = Field(max_length=45, nullable=True)

    postal_code: Optional[str] = Field(max_length=45, nullable=True)

    is_active: Optional[int] = Field(default=1)

    total_buy: int = Field(default=0)



# Define the SQLModel class
class supplier(SupplierBase, table=True):
    """Customer Base Class"""

    id: Optional[int] = Field(default=None, index=True, primary_key=True)

    created_at: Optional[datetime] = Field(sa_column=Column(
        DateTime(timezone=True),
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP"),
    ))

    updated_at: Optional[datetime] = Field(sa_column=Column(
        DateTime(timezone=True),
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP"),
        onupdate=datetime.utcnow,
    ))

SQLModel.metadata.create_all(engine)
