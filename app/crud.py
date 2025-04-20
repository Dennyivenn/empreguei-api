# app/crud.py
from sqlalchemy.orm import Session
from app.models import User

def create_user(db: Session, user_data):
    db_user = User(username=user_data.username, email=user_data.email, password=user_data.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()
