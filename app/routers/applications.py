from fastapi import APIRouter

router = APIRouter()

@router.get("/applications")
def get_applications():
    return {"message": "List of applications"}
