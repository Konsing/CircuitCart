from fastapi import Depends, APIRouter, HTTPException, status
from typing import Annotated
from sqlalchemy.orm import Session
from ..dependencies import db_dependency

router = APIRouter(
    prefix="/products",
    tags=["Products"]    
)


@router.get("/products", description="")
def get_products(db: db_dependency):
    return {'message': 'List of products will appear here.'}