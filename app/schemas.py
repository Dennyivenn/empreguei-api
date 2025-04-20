# app/schemas.py
from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class JobBase(BaseModel):
    title: str
    description: str

class JobCreate(JobBase):
    pass

class Job(JobBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class ApplicationBase(BaseModel):
    cover_letter: str

class ApplicationCreate(ApplicationBase):
    pass

class Application(ApplicationBase):
    id: int
    job_id: int
    user_id: int

    class Config:
        orm_mode = True
