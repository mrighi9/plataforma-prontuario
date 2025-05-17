from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models
from app.schemas.user import UserCreate, UserRead
from app.crud.user import (
    criar_user, listar_users, buscar_user_por_id,
    deletar_user
)

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=UserRead)
def criar(user: UserCreate, db: Session = Depends(get_db)):
    return criar_user(db, user)

@app.get("/users/", response_model=list[UserRead])
def listar(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return listar_users(db, skip, limit)

@app.get("/users/{user_id}", response_model=UserRead)
def buscar(user_id: int, db: Session = Depends(get_db)):
    user = buscar_user_por_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return user

@app.delete("/users/{user_id}")
def deletar(user_id: int, db: Session = Depends(get_db)):
    user = deletar_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
    return {"ok": True}
