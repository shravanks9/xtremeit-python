"""Application routes"""
from typing import Optional
import logging
import json
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import Session, select
from fastapi.encoders import jsonable_encoder

from lib.database import get_session
from models.cart import cart,CartSkeleton

router = APIRouter()

logger = logging.getLogger('infinity-logger')


class ResponseModel(BaseModel):
    data: dict


@router.post("/cart", response_model=CartSkeleton)
def create_projectmembers(projectmembers: cart,
                          session: Session = Depends(get_session)):

    projectmembers = cart.from_orm(projectmembers)
    session.add(projectmembers)
    session.commit()
    session.refresh(projectmembers)

    return projectmembers


@router.get("/cart")
async def get_cart(limit: Optional[int] = 50, session: Session = Depends(get_session)):
    # category= session.query(cart).filter(cart.id == id).first()
    query = select(cart)
    if limit:
        query = query.limit(limit)
    cart_data = session.exec(query).all()
    if cart_data:
        return jsonable_encoder(cart_data)
    else:
        return {"data": "not found"}


@router.put("/cart/{category_id}")
async def update_category(category_id: int, category_update:cart,session: Session = Depends(get_session)):
    category = session.query(cart).filter(cart.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    update_data = category_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(category, key, value)
    session.add(category)
    session.commit()
    session.refresh(category)
    
    return update_data


@router.delete("/cart/{id}")
async def delete_category(id: int, db: Session = Depends(get_session)):
    # Fetch the category to delete
    try:
        db_category = db.query(cart).filter(cart.id == id).first()

        if db_category:
            # Delete the category
            db.delete(db_category)

            # Commit the changes to the database
            db.commit()

            # Return a success message
            return {"message": "Category deleted successfully"}

        # If the category is not found, raise an HTTPException
        raise HTTPException(status_code=404, detail="Category not found")

    except Exception as error:
        # Log the error and raise an HTTPException with a 500 status code
        logger.exception(error)
        raise HTTPException(status_code=500, detail="foreign key relation cannot be deleted")