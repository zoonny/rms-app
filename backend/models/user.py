from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.base import BaseModel
from models.permission import user_permission

class User(BaseModel):
    # postgres에서 user 테이블 사용, 복수형 예외처리
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True)
    permissions = relationship(
        'Permission',
        secondary=user_permission,
        back_populates='users'
    )
    
