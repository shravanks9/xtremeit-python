"""Crm Models"""
from datetime import datetime
from typing import Optional

from sqlmodel import  DateTime, Column, Field, SQLModel, text

from lib.database import engine

class SubCategorySkeleton(SQLModel):
    
    name: str = Field(default=None,max_length=100, nullable=False)
    
    slug: str = Field(default=None,max_length=45, nullable=True)

    category_id:Optional[int]= Field (default=None,nullable=False)
    
class SubCategoryBase(SubCategorySkeleton):
    
    short_description: str = Field(default=None,max_length=500, nullable=True)
    
    full_description: str = Field(default=None, max_length=10000, nullable=True)
    
    tags: str = Field(default=None, max_length=100, nullable=True)


class subcategories(SubCategoryBase,table=True):
    
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