"""Application routes"""
from typing import Optional
import logging
from fastapi import APIRouter, Depends,HTTPException
# from pydantic import BaseModel
from sqlmodel import Session,select
from fastapi.encoders import jsonable_encoder

from lib.database import get_session
from models.sub_catagory import sub_categories 
from  models.category import categories
router = APIRouter()

logger = logging.getLogger('infinity-logger')

@router.post("/sub-categories", response_model=dict)
def create_projectmembers(projectmembers: sub_categories,
                       session: Session = Depends(get_session)):

    projectmembers = sub_categories.from_orm(projectmembers)
    session.add(projectmembers)
    session.commit()
    session.refresh(projectmembers)

    return projectmembers



@router.get("/sub-categories")
async def get_sub_categories( limit: Optional[int] = 50,session: Session = Depends(get_session)):
    query = select(sub_categories)
    if limit:
        query = query.limit(limit)
    sub_category = session.exec(query).all()
    if sub_category:
        return jsonable_encoder(sub_category)
    else:
        return {"data": "not found"}


@router.put("/sub-categories/{category_id}")
async def update_category(category_id: int, category_update:sub_categories,session: Session = Depends(get_session)):
    category = session.query(sub_categories).filter(sub_categories.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    update_data = category_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(category, key, value)
    session.add(category)
    session.commit()
    session.refresh(category)
    
    return update_data

@router.delete("/sub-categories/{id}")
async def delete_sub_category(id: int, db: Session = Depends(get_session)):
    # Fetch the category to delete
    try:
        db_category = db.query(sub_categories).filter(sub_categories.id == id).first()

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