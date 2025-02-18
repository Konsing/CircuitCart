from fastapi import Depends, APIRouter, HTTPException, status
from typing import Annotated
from sqlalchemy.orm import Session
from ..dependencies import db_dependency

router = APIRouter(
    prefix="/health",
    tags=["Health"]    
)


@router.get("/system_status", description="")
def get_system_status():
    return {'status': 'ok'}