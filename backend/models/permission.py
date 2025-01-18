from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base import BaseModel

user_permission = Table(
    'user_permission',
    BaseModel.metadata,
    Column('user_id', Integer, ForeignKey('users.id'), primary_key=True),
    Column('permission_id', Integer, ForeignKey('permission.id'), primary_key=True)
)

class Permission(BaseModel):
    __tablename__ = "permission"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    users = relationship(
        'User',
        secondary=user_permission,
        back_populates='permissions'
    )
