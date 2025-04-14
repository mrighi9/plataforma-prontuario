from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import Usuario

# Inicializa as tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Função para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint para criar um usuário
@app.post("/usuarios/")
def criar_usuario(nome: str, email: str, db: Session = Depends(get_db)):
    novo_usuario = Usuario(nome=nome, email=email)
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

# Endpoint para listar usuários
@app.get("/usuarios/")
def listar_usuarios(db: Session = Depends(get_db)):
    return db.query(Usuario).all()
