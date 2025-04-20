from app.database import engine, Base
from app.models import usuario
# Criação das tabelas no banco de dados
Base.metadata.create_all(bind=engine)  # Vai criar todas as tabelas definidas com o SQLAlchemy