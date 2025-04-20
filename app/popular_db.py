import sys
import os
from sqlalchemy.orm import Session
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import engine
from app.models.usuario import Usuario
from app.models.vaga import Vaga
from app.models.candidatura import Candidatura

# Criar sessão
from sqlalchemy.orm import sessionmaker

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Inserir usuários de exemplo (com campo tipo)
usuario1 = Usuario(nome="João", email="joao@email.com", senha="senha123", tipo="empresa")
usuario2 = Usuario(nome="Maria", email="maria@email.com", senha="senha456", tipo="candidato")

session.add_all([usuario1, usuario2])
session.commit()

# Inserir vagas
vaga1 = Vaga(titulo="Desenvolvedor Python", descricao="Trabalhar com APIs", empresa_id=usuario1.id, usuario_id=usuario1.id)
vaga2 = Vaga(titulo="Designer UI/UX", descricao="Design para web", empresa_id=usuario1.id, usuario_id=usuario2.id)

session.add_all([vaga1, vaga2])
session.commit()

# Inserir candidatura
candidatura1 = Candidatura(usuario_id=usuario2.id, vaga_id=vaga1.id)
session.add(candidatura1)
session.commit()

print("Dados inseridos com sucesso!")
session.close()
