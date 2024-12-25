from sqlalchemy import create_engine, Column, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "postgresql://stgbsuser:sideV1234!@10.97.226.87:5432/stgbsdb"
# DATABASE_URL = "postgresql://stgbsuser:sideV1234!@52.231.105.193:31432/stgbsdb"
DATABASE_URL = "postgresql://stgbsuser:sideV1234!@host.docker.internal:5432/stgbsdb"

engine = create_engine(DATABASE_URL)

# db logging
import logging
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.ERROR)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
