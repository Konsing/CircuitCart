from fastapi import Depends, APIRouter, HTTPException, status
from typing import Annotated
from sqlalchemy.orm import Session
from ..dependencies import db_dependency

router = APIRouter(
    prefix="/cart",
    tags=["Cart"]    
)


@router.get("/cart_items", description="")
def get_cart_items(db: db_dependency):
    return {'message': 'List of cart items will appear here.'}