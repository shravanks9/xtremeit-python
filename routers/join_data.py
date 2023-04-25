from fastapi import APIRouter,Depends
from models.join_table import jointable
from sqlmodel import select,Session
from lib.database import get_session
from models.cart import cart
from models.customer import customer
from  models.product import products




router=APIRouter()

@router.get("/join-data")
async def get_join_data(limit:int=50,session:Session=Depends(get_session)):
    jointable.product_id=products.id
    jointable.product_name=products.name
    jointable.price=products.price
    jointable.quantity=products.quantity
    jointable.customer_id=customer.id
    jointable.first_name=customer.fname
    jointable.last_name=customer.lname
    jointable.email=customer.email
    jointable.phone_number=customer.phone_number
    jointable.cart_id=cart.id
    jointable.status=cart.status
    jointable.is_active=customer.is_active
    s
    query=select(jointable)
    join_data=session.exec(query).all()

# query = (
#         select(Cart, Customer, Product)
#         .join(Customer, Customer.id == Cart.customer_id)
#         .join(Product, Product.id == Cart.product_id)
#         .limit(limit)
#     )
#     join_data = session.exec(query).all()
#     return join_data
    
    