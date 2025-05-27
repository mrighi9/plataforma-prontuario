# app/routes/auth.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import user as user_schema
from app.crud import user as user_crud
from app.database import get_db
from app.auth.hashing import Hash
from app.auth.jwt import create_access_token

router = APIRouter(prefix="/auth", tags=["Autenticação"])

@router.post("/register", response_model=user_schema.UserOut)
def register(user: user_schema.UserCreate, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email já registrado")
    return user_crud.create_user(db, user)

@router.post("/login")
def login(user: user_schema.UserLogin, db: Session = Depends(get_db)):
    db_user = user_crud.get_user_by_email(db, user.email)
    if not db_user:
        print(f"Usuário não encontrado: {user.email}")
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    if not Hash.verify(user.password, db_user.hashed_password):
        print(f"Senha incorreta para o usuário: {user.email}")
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    print(f"Login bem-sucedido para o usuário: {user.email}")
    token = create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}
