from pydantic import BaseModel

class jointable(BaseModel):
    product_id:str
    product_name:str
    price:str
    quantity:str
    customer_id:str
    first_name:str
    last_name:str
    email:str
    phone_number:str
    cart_id:str
    status:str
    is_active:str
    