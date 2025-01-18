from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import BaseModel
from models.permission import user_permission

class User(BaseModel):
    # postgres에서 user 테이블 사용, 복수형 예외처리
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, index=True, unique=True)
    name = Column(String, index=True)
    hashed_password = Column(String)
    is_active = Column(Integer, default=1)
    permissions = relationship(
        'Permission',
        secondary=user_permission,
        back_populates='users'
    )
    
