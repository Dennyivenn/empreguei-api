from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, models
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/usuarios")
def read_usuarios(db: Session = Depends(get_db)):
    return crud.get_usuarios(db)
