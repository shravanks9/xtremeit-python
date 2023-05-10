"""Cart Models"""
from datetime import datetime
from typing import Optional

from sqlmodel import  DateTime, Column, Field, SQLModel, text

from lib.database import engine


class CartSkeleton(SQLModel):
    
    quantity: int = Field(default=None, nullable=True)

    status: bool = Field(default=None, nullable=False)
    
    customer_id: int = Field(default=None, nullable=False)

    product_id: int = Field(default=None, nullable=False)
    

class cart(CartSkeleton,table=True):
    
    
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