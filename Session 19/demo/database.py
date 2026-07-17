from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "mysql+pymysql://root:Quangan310820@localhost:3306/student_db"

Base = declarative_base()

engine = create_engine(DB_URL)

LocalSesssion = sessionmaker(
    autoflush=False,
    bind=engine,
    expire_on_commit=False
)

def get_db():
    db = LocalSesssion()
    try:
        yield db
    finally:
        db.close()