from sqlalchemy import Column, Integer, String, CheckConstraint
from app.database import Base


class User(Base):
    __tablename__ = "users"          # opcional: mantenha “usuario” se quiser

    id       = Column(Integer, primary_key=True, index=True)
    name     = Column(String(100), nullable=False)
    email    = Column(String(100), nullable=False, unique=True, index=True)
    password = Column(String(255), nullable=False)
    cpf      = Column(String(14),  nullable=False)
    role     = Column(String(1),   nullable=False)   # 'A' admin, 'M' medic etc.

    __table_args__ = (
        CheckConstraint(
            r"cpf ~ '^[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}$'",
            name="user_cpf_format_check",
        ),
    )
