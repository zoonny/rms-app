from sqlalchemy import Column, DateTime, func
from db.database import Base

class BaseModel(Base):
    __abstract__ = True  # 상속용 추상 클래스
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)