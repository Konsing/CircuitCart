from fastapi import Depends, APIRouter, HTTPException, status
from typing import Annotated
from sqlalchemy.orm import Session
from ..dependencies import db_dependency

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]    
)

@router.post("/register", description="Creates a new user account and returns an access token.")
def register_user(db: db_dependency):
    # Registration logic here
    pass

@router.post("/login", description="Authenticates a user and returns an access token.")
def login_user(db: db_dependency):
    # Login logic here
    pass

@router.post("/logout", description="Logs out the user.")
def logout_user(db: db_dependency):
    # Logout logic here
    pass