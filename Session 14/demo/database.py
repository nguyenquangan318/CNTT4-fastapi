from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = "mysql+pymysql://root:Quangan310820@localhost:3306/test_db"

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