from fastapi import Depends, APIRouter, HTTPException, status
from typing import Annotated
from sqlalchemy.orm import Session
from ..dependencies import db_dependency

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]    
)


@router.post("/register", description="Creates a new user account with the provided data and returns an access token for authentication.")
def register_user(db: db_dependency):
    pass


@router.post("/login", description="Authenticates a user with their email and password. Returns an access token if the credentials are correct.")
def login_user(db: db_dependency):
    pass


@router.post("/logout", description="Authenticates a user with their email and password. Returns an access token if the credentials are correct.")
def logout_user(db: db_dependency):
    pass