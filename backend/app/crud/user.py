from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def criar_user(db: Session, user: UserCreate):
    db_user = User(
        nome=user.nome,
        email=user.email,
        senha=get_password_hash(user.senha),
        cpf=user.cpf,
        perfil=user.perfil
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def listar_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def buscar_user_por_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def buscar_user_por_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def deletar_user(db: Session, user_id: int):
    user = buscar_user_por_id(db, user_id)
    if user:
        db.delete(user)
        db.commit()
    return user
