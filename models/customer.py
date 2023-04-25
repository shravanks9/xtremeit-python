from datetime import datetime
from typing import Optional

from sqlmodel import Column, Field, SQLModel, TIMESTAMP, text, Date,DateTime

from lib.database import engine


# Define the SQLModel configuration object
class Config:
    arbitrary_types_allowed = True
    ...

# Define the SQLModel class
class customer(SQLModel, table=True):
    """Customer Base Class"""

    id: Optional[int] = Field(default=None, index=True, primary_key=True)

    fname: Optional[str] = Field(max_length=50, nullable=False)

    lname: Optional[str] = Field(max_length=50, nullable=True)

    username: Optional[str] = Field(max_length=100, nullable=False)

    password: Optional[str] = Field(max_length=100, nullable=False)

    image_url: Optional[str] = Field(max_length=1024, nullable=True)

    birthdate: Optional[str] = Field(nullable=True)

    email: Optional[str] = Field(max_length=100, nullable=True)

    email1: Optional[str] = Field(max_length=100, nullable=True)

    email2: Optional[str] = Field(max_length=100, nullable=True)

    address: Optional[str] = Field(max_length=500, nullable=True)

    address1: Optional[str] = Field(max_length=500, nullable=True)

    address2: Optional[str] = Field(max_length=500, nullable=True)

    phone_number: Optional[str] = Field(max_length=45, nullable=True)

    phone_number1: Optional[str] = Field(max_length=45, nullable=True)

    is_active: Optional[int] = Field(default=1)

    total_buy: int = Field(default=0)

    twitter_id: Optional[str] = Field(max_length=100, nullable=True)

    linkedin_id: Optional[str] = Field(max_length=100, nullable=True)

    facebook_id: Optional[str] = Field(max_length=100, nullable=True)

    skype_id: Optional[str] = Field(max_length=100, nullable=True)

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