from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from app.database import SessionLocal, engine
from . import models  # Corrige a importação do módulo `models`
from app.schemas.user import UserCreate, UserRead
from app.crud.user import (
    create_user,
    list_users,
    get_user_by_id,
    delete_user,
)
from app.routes import auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Prontuario Médico API")


# Configuração de CORS
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "http://localhost:5173",  # Porta padrão do Vite
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --------------------- Dep -----------------------------

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# --------------------- Endpoints -----------------------

@app.post("/users/", response_model=UserRead, status_code=201)
def create(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@app.get("/users/", response_model=list[UserRead])
def read_all(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return list_users(db, skip, limit)


@app.get("/users/{user_id}", response_model=UserRead)
def read_one(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@app.delete("/users/{user_id}", status_code=204)
def remove(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return None


# Inclui o roteador de autenticação
app.include_router(auth.router)
