from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Obtendo a URL do banco de dados do arquivo .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Configurar a conexão com o banco de dados
engine = create_engine(DATABASE_URL)

# Criando a base de dados
Base = declarative_base()

# Criar uma sessão para interagir com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Função para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
