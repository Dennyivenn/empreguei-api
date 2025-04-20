from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import users, jobs, applications  # Importando as rotas

app = FastAPI()

# ✅ Adicionando CORS para liberar POST, PUT, DELETE de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou troque "*" por ["https://empreguei.co.mz"] no futuro
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Registrando as rotas
app.include_router(users.router)
app.include_router(jobs.router)
app.include_router(applications.router)
