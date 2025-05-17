# backend/app/models/__init__.py
from app.database import Base               # expõe Base (declarative_base)

# importe todos os modelos individuais aqui
from .user import User

__all__ = ["Base", "User"]
