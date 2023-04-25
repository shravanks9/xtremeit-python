"""Crm Models"""
import enum
import uuid as uuid_pkg
from datetime import datetime
from typing import Optional

from sqlmodel import  TIMESTAMP, Column, Enum, Field, SQLModel, text,Integer,ForeignKey

from lib.database import engine


class sub_categories(SQLModel ,table=True):
    """ Project Members Base Class """
    id: Optional[int] = Field(default=None,  index=True, primary_key=True)

    name: str = Field(default=None,max_length=100, nullable=False)

    # Project Id
    slug: str = Field(default=None,max_length=45, nullable=True)

    # Member Id
    short_description: str = Field(default=None,max_length=500, nullable=True)

    # Project Member Role
    full_description: str = Field(default=None, max_length=10000, nullable=True)

    # Project Member Role
    tags: str = Field(default=None, max_length=100, nullable=True)

    category_id:Optional[int]= Field (default=None,nullable=False)

    # Project Creation Date
    created_at: Optional[datetime] = Field(sa_column=Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    ))

    # Project Updation date
    updated_at:  Optional[datetime] = Field(sa_column=Column(
        TIMESTAMP(timezone=True),
        nullable=False,
        server_default=text("CURRENT_TIMESTAMP"),
    ))


SQLModel.metadata.create_all(engine)
