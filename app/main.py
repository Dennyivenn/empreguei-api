from fastapi import FastAPI
from app.routers import users, jobs, applications

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API Empreguei.co.mz está rodando!"}

app.include_router(users.router)
app.include_router(jobs.router)
app.include_router(applications.router)
