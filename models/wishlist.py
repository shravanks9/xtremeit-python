"""Crm Models"""
from datetime import datetime
from typing import Optional

from sqlmodel import  TIMESTAMP, Column, Field, SQLModel, text

from lib.database import engine

class WishlistSkeleton(SQLModel):
    
    customer_id: int = Field(default=None, nullable=False)

    product_id: int = Field(default=None, nullable=False)

    status: bool = Field(default=None, nullable=False)

class wishlist( WishlistSkeleton,table=True):
        
    id: Optional[int] = Field(default=None,  index=True, primary_key=True)

    
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