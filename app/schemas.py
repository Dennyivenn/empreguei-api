from pydantic import BaseModel
from typing import List, Optional

# Schema para criar usuários
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class User(UserCreate):
    id: int

    class Config:
        orm_mode = True

# Schema para criar vagas
class JobCreate(BaseModel):
    title: str
    description: str
    company: str

class Job(JobCreate):
    id: int

    class Config:
        orm_mode = True

# Schema para criar candidaturas
class ApplicationCreate(BaseModel):
    job_id: int
    user_id: int

class Application(ApplicationCreate):
    id: int

    class Config:
        orm_mode = True
