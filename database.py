from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from app import models
from dotenv import load_dotenv
import os

# Carregar as variáveis do .env
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Criação do engine para o banco de dados
engine = create_engine(DATABASE_URL)

# Criação da base de dados
Base = declarative_base()

# Criando a sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
