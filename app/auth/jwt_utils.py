# app/auth/jw_utilis.py
from fastapi import HTTPException
from fastapi.security import OAuth2PasswordBearer
from jwt import PyJWTError
from jose import jwt
from app.models import Usuario

# Defina a chave secreta e o algoritmo de codificação
SECRET_KEY = "seu_segredo_aqui"
ALGORITHM = "HS256"

# Instância o OAuth2PasswordBearer para pegar o token do header Authorization
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_token(token: str = Depends(oauth2_scheme)):
    try:
        # Decodifica o token JWT
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        
        # Valida se o usuário existe no banco de dados
        db_user = Usuario.query.filter(Usuario.username == username).first()
        if db_user is None:
            raise HTTPException(status_code=401, detail="Usuário não encontrado")
        
        return payload  # Retorna as informações do payload do token (como o nome de usuário)
    
    except PyJWTError:
        raise HTTPException(status_code=401, detail="Token inválido")
