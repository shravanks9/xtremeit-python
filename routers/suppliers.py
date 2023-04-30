from typing import Optional
import logging
import json
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlmodel import Session

from lib.database import get_session
from lib.util import create_jwt
from models.suppliers import supplier,SupplierSkeleton

router = APIRouter()

logger = logging.getLogger('infinity-logger')


class JWTResponse(BaseModel):
    jwt: str


@router.post("/signup", response_model=JWTResponse)
def create_supplier(supplier_data: SupplierSkeleton,
                          session: Session = Depends(get_session)):

    supplier_data = supplier.from_orm(supplier_data)

    session.add(supplier_data)
    session.commit()
    session.refresh(supplier_data)

    data={"id":supplier_data.id,
          "user_name":supplier_data.username,
          "email":supplier_data.email,
          "type":"supplier"}
    
    jwt=create_jwt(data)

    return {"jwt":jwt}


@router.get("/login",response_model=JWTResponse)
async def get_supplier(user_name: str,password: str, session: Session = Depends(get_session)):

    supplier_data = session.query(supplier).filter(supplier.username == user_name).first()

    if not supplier_data or (supplier_data.password!=password):
        raise HTTPException(status_code=400,detail="Inalid User name/Password")
    
    data={"id":supplier_data.id,
          "user_name":supplier_data.username,
          "email":supplier_data.email,
          "type":"supplier"}
    
    jwt=create_jwt(data)

    return {"jwt":jwt}