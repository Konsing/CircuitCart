from fastapi import Depends, APIRouter, HTTPException, status
from typing import Annotated
from sqlalchemy.orm import Session
from ..dependencies import db_dependency

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]    
)


@router.get("/orders", description="")
def get_orders(db: db_dependency):
    return {'message': 'List of user orders will appear here.'}