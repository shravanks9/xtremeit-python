"""Application routes"""
from typing import Optional
import logging
from fastapi import APIRouter, Depends,HTTPException

from sqlmodel import Session,select
from fastapi.encoders import jsonable_encoder
from lib.database import get_session
from models.product import ProductBase,products,ProductSkeleton


router = APIRouter()

logger = logging.getLogger('infinity-logger')

@router.post("/products", response_model=ProductSkeleton)
def create_projectmembers(projectmembers: ProductBase,
                       session: Session = Depends(get_session)):

    projectmembers = products.from_orm(projectmembers)
    session.add(projectmembers)
    session.commit()
    session.refresh(projectmembers)

    return projectmembers


@router.get("/products")
async def get_products( limit: Optional[int] = 50,session: Session = Depends(get_session)):
    query = select(products)
  
    product = session.exec(query).all()
    if product:
        return jsonable_encoder(product)
    else:
        return {"data": "not found"}

@router.put("/products/{category_id}")
async def update_category(category_id: int, category_update:products,session: Session = Depends(get_session)):
    category = session.query(products).filter(products.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    update_data = category_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(category, key, value)
    session.add(category)
    session.commit()
    session.refresh(category)
    
    return update_data

@router.delete("/products/{id}")
async def delete_products(id: int, db: Session = Depends(get_session)):
    # Fetch the category to delete
    try:
        db_category = db.query(products).filter(products.id == id).first()

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