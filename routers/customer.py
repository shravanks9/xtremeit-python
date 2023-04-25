"""Application routes"""
from typing import Optional
import logging
import json
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import Session, select
from fastapi.encoders import jsonable_encoder

from lib.database import get_session
from models.customer import customer

router = APIRouter()

logger = logging.getLogger('infinity-logger')


class ResponseModel(BaseModel):
    data: dict


@router.post("/customer", response_model=dict)
def create_customer(projectmembers: customer,
                          session: Session = Depends(get_session)):

    projectmembers = customer.from_orm(projectmembers)
    session.add(projectmembers)
    session.commit()
    session.refresh(projectmembers)

    return projectmembers


@router.get("/customer")
async def get_customer(limit: Optional[int] = 50, session: Session = Depends(get_session)):
    # category= session.query(customer).filter(customer.id == id).first()
    query = select(customer).limit(limit)

    categorie = session.exec(query).all()
    if categorie:
        return jsonable_encoder(categorie)
    else:
        return {"data": "not found"}
    

@router.get("/login")
async def get_customer(user_name: str,password: str, session: Session = Depends(get_session)):
    category= session.query(customer).filter(customer.username == user_name, customer.password == password).first()

    if not category:
        raise Exception("user not found")
    return category


@router.put("/customer/{category_id}")
async def update_category(category_id: int, category_update:customer,session: Session = Depends(get_session)):
    category = session.query(customer).filter(customer.id == category_id).first()
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    
    update_data = category_update.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(category, key, value)
    session.add(category)
    session.commit()
    session.refresh(category)
    
    return update_data


@router.delete("/customer/{id}")
async def delete_category(id: int, db: Session = Depends(get_session)):
    # Fetch the category to delete
    try:
        db_category = db.query(customer).filter(customer.id == id).first()

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