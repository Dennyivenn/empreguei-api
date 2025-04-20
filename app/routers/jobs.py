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

# Rota para obter todas as vagas
@router.get("/vagas")
def read_vagas(db: Session = Depends(get_db)):
    return crud.get_vagas(db)

# Rota para criar uma nova vaga
@router.post("/vagas")
def create_vaga(titulo: str, descricao: str, db: Session = Depends(get_db)):
    return crud.create_vaga(db, titulo=titulo, descricao=descricao)

# Rota para atualizar uma vaga
@router.put("/vagas/{vaga_id}")
def update_vaga(vaga_id: int, titulo: str = None, descricao: str = None, db: Session = Depends(get_db)):
    return crud.update_vaga(db, vaga_id, titulo, descricao)

# Rota para deletar uma vaga
@router.delete("/vagas/{vaga_id}")
def delete_vaga(vaga_id: int, db: Session = Depends(get_db)):
    db_vaga = crud.delete_vaga(db, vaga_id)
    if db_vaga is None:
        raise HTTPException(status_code=404, detail="Vaga não encontrada")
    return {"message": "Vaga deletada com sucesso"}
