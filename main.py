from fastapi import FastAPI
from app.routers import applications  # Supondo que você tenha o arquivo applications.py dentro de 'routers'

app = FastAPI()

# Inclui as rotas definidas em applications.py
app.include_router(applications.router)
