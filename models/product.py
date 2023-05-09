"""Products Models"""
from datetime import datetime
from typing import Optional
# from models.sub_category import sub_categories
from sqlmodel import  DateTime, Column, Field, SQLModel, text
from lib.database import engine


class ProductSkeleton(SQLModel):
    
    name: str = Field(default=None,max_length=100, nullable=True)
    
    slug: str = Field(default=None,max_length=45, nullable=True)
    
    price : float =Field(default=None,nullable=True)

    quantity: int=Field(default=None,nullable=True)
    
    sub_category_id: Optional[int] = Field(default=None,nullable=True)

    
class ProductBase(ProductSkeleton):
    
    short_description: str = Field(default=None,max_length=500, nullable=True)
   
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

    

class products(ProductBase,table=True):
    
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
