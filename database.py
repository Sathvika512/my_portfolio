
from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# Get the current project folder
BASE_DIR = Path(__file__).resolve().parent

# Database file path
DATABASE_URL = f"sqlite:///{BASE_DIR / 'portfolio.db'}"


# Create database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)


# Create database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for ORM models
Base = declarative_base()


# Database dependency
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
