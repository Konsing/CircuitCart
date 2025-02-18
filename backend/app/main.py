from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import Annotated
from . import models
from .config.database import engine, get_db
from .routes.cart import router as cart_router
from .routes.auth import router as auth_router
from .routes.health import router as health_router
from .routes.products import router as products_router 

# models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost:3000",
]

app = FastAPI(
    title="CircuitCart Backend",
    description="shitty ass website to sell tech components",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # or use ["*"] to allow all origins during development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/", tags=["System"], description="Provides a welcome message and confirms that the API is running.")
def read_root():
    return {"message": "Welcome to the CircuitCart"}

app.include_router(cart_router)
app.include_router(auth_router)
app.include_router(health_router)
app.include_router(products_router)