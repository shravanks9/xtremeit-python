
from fastapi import FastAPI,Request
from routers  import category, connection,product, sub_category,upload_file,customer,cart,wishlist
import time
from fastapi.middleware.cors import CORSMiddleware

app=FastAPI()
from fastapi import FastAPI, Request
import time
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

from lib.database import engine,create_db_tables

app.include_router(tags=["products"], router=product.router)

app.include_router(tags=["category"], router=category.router)

app.include_router(tags=["sub_category"], router=sub_category.router)

app.include_router(tags=["connection"], router=connection.router)

app.include_router(tags=["upload_file"],router=upload_file.router)

app.include_router(tags=["customer"], router=customer.router)

app.include_router(tags=["cart"], router=cart.router)

app.include_router(tags=["wishlist"], router=wishlist.router)

# app.include_router(tags=["sub_category"], router=connection.router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
