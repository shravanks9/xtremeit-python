"""Crm Models"""
import enum
import uuid as uuid_pkg
from datetime import datetime
from typing import Optional
from models.sub_catagory import sub_categories
from sqlmodel import  TIMESTAMP, Column, Enum, Field, SQLModel, text,Relationship
from lib.database import engine


class products(SQLModel ,table=True):
    """ Project Members Base Class """
    id: Optional[int] = Field(default=None,  index=True, primary_key=True)

    name: str = Field(default=None,max_length=100, nullable=True)

    # Project Id
    slug: str = Field(default=None,max_length=45, nullable=True)

    # Member Id
    short_description: str = Field(default=None,max_length=500, nullable=True)

    price : float =Field(default=None,nullable=True)

    quantity: int=Field(default=None,nullable=True)
   
    full_detail: str = Field(default=None, max_length=10000, nullable=True)
  
    tags: str = Field(default=None, max_length=100, nullable=True)
    
    image_url: str = Field(default=None, max_length=100, nullable=True)

    image_url1: str = Field(default=None, max_length=100, nullable=True)
    
    image_url2: str = Field(default=None, max_length=100, nullable=True)

    image_url3: str = Field(default=None, max_length=100, nullable=True)
    
    image_url4: str = Field(default=None, max_length=100, nullable=True)
    
    image_url5: str = Field(default=None, max_length=100, nullable=True)
    
    image_url6: str = Field(default=None, max_length=100, nullable=True)
    
    SKU :str = Field(default=None,max_length=500,nullable=True)
    
    IDSKU :str = Field(default=None,max_length=500,nullable=True)

    sub_category_id: Optional[int] = Field(default=None,nullable=True)
    
  

    # Project Creation Date
    created_at: Optional[datetime] = Field(sa_column=Column(
        TIMESTAMP(timezone=True),
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP"),
    ))

    # Project Updation date
    updated_at:  Optional[datetime] = Field(sa_column=Column(
        TIMESTAMP(timezone=True),
        nullable=True,
        server_default=text("CURRENT_TIMESTAMP"),
    ))


SQLModel.metadata.create_all(engine)
