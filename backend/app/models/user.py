from sqlalchemy import Column, Integer, String, CheckConstraint
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuario"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    senha = Column(String(255), nullable=False)
    cpf = Column(String(14), nullable=False)
    perfil = Column(String(1), nullable=False)  # Ex: 'A' para admin, 'M' para médico etc.

    __table_args__ = (
        CheckConstraint(
            "cpf ~ '^[0-9]{3}\\.[0-9]{3}\\.[0-9]{3}-[0-9]{2}$'",
            name="usuario_cpf_check"
        ),
    )
