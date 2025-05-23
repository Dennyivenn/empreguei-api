from sqlalchemy import Column, Integer, String
from app.database import Base

class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    senha = Column(String)
    tipo = Column(String, nullable=False)  # Adicionando o campo tipo com a restrição 'NOT NULL'
