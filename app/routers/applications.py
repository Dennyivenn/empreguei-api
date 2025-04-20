from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from .. import crud, models
from ..database import SessionLocal

router = APIRouter()

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rota para obter todas as candidaturas
@router.get("/candidaturas")
def read_candidaturas(db: Session = Depends(get_db)):
    return crud.get_candidaturas(db)

# Rota para criar uma nova candidatura
@router.post("/candidaturas")
def create_candidatura(usuario_id: int, vaga_id: int, db: Session = Depends(get_db)):
    return crud.create_candidatura(db, usuario_id=usuario_id, vaga_id=vaga_id)

# Rota para deletar uma candidatura
@router.delete("/candidaturas/{candidatura_id}")
def delete_candidatura(candidatura_id: int, db: Session = Depends(get_db)):
    db_candidatura = crud.delete_candidatura(db, candidatura_id)
    if db_candidatura is None:
        raise HTTPException(status_code=404, detail="Candidatura não encontrada")
    return {"message": "Candidatura deletada com sucesso"}
