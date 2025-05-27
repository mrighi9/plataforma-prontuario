import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL  = os.getenv("DATABASE_URL")
SSL_ROOT_CERT = os.getenv("SSL_ROOT_CERT")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL não está definido no arquivo .env")

connect_args = {
    "sslmode": "require",
    "sslrootcert": SSL_ROOT_CERT,
}

engine = create_engine(
    DATABASE_URL,
    connect_args=connect_args,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
