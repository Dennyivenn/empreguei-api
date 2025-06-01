from sqlalchemy.orm import Session
from . import models
import bcrypt  # Se estiver utilizando bcrypt para criptografar as senhas

# Função para obter todos os usuários
def get_usuarios(db: Session):
    return db.query(models.Usuario).all()

# Função para obter o usuário pelo email
def get_user_by_email(db: Session, email: str):
    return db.query(models.Usuario).filter(models.Usuario.email == email).first()

# Função para criar um novo usuário
def create_usuario(db: Session, nome: str, email: str, senha: str):
    hashed_password = bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt())  # Criptografa a senha
    db_usuario = models.Usuario(nome=nome, email=email, senha=hashed_password)
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

# Função para verificar se a senha fornecida é válida
def verify_password(stored_password: str, provided_password: str):
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))

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
