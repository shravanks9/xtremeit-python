"""Application routes"""
from typing import Optional
import logging
import json
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import Session, select
from fastapi.encoders import jsonable_encoder

from lib.database import get_session,engine
from models.wishlist import WishlistSkeleton,wishlist

router = APIRouter()

logger = logging.getLogger('infinity-logger')


class ResponseModel(BaseModel):
    data: dict


@router.post("/wishlist", response_model=dict)
def create_projectmembers(projectmembers: wishlist):

    projectmembers = wishlist.from_orm(projectmembers)
    with Session(engine) as session :
        session.add(projectmembers)
        session.commit()
        session.refresh(projectmembers)
    
    return projectmembers


@router.get("/wishlist")
async def get_wishlist(limit: Optional[int] = 50, session: Session = Depends(get_session)):
    # category= session.query(wishlist).filter(wishlist.id == id).first()
    query = select(wishlist)
    if limit:
        query = query.limit(limit)
    categorie = session.exec(query).all()
    if categorie:
        return jsonable_encoder(categorie)
    else:
        return {"data": "not found"}


@router.put("/wishlist/{category_id}")
async def update_category(category_id: int, category_update:wishlist,session: Session = Depends(get_session)):
    category = session.query(wishlist).filter(wishlist.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    update_data = category_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(category, key, value)
    session.add(category)
    session.commit()
    session.refresh(category)
    
    return update_data


@router.delete("/wishlist/{id}")
async def delete_category(id: int, db: Session = Depends(get_session)):
    # Fetch the category to delete
    try:
        db_category = db.query(wishlist).filter(wishlist.id == id).first()

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