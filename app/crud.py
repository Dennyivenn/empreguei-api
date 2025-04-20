from sqlalchemy.orm import Session
from . import models

# Função para obter todos os usuários
def get_usuarios(db: Session):
    return db.query(models.Usuario).all()

# Função para criar um novo usuário
def create_usuario(db: Session, nome: str, email: str):
    db_usuario = models.Usuario(nome=nome, email=email)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

# Função para atualizar um usuário
def update_usuario(db: Session, usuario_id: int, nome: str, email: str):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if db_usuario:
        db_usuario.nome = nome if nome else db_usuario.nome
        db_usuario.email = email if email else db_usuario.email
        db.commit()
        db.refresh(db_usuario)
        return db_usuario
    return None

# Função para deletar um usuário
def delete_usuario(db: Session, usuario_id: int):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if db_usuario:
        db.delete(db_usuario)
        db.commit()
        return db_usuario
    return None
