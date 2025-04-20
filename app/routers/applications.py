from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def listar_vagas():
    return {"msg": "Lista de vagas"}
