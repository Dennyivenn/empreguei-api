from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def listar_usuarios():
    return {"msg": "Lista de usuários"}
