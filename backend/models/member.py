from sqlalchemy import Column, Integer, String
from models.base import BaseModel

class Member(BaseModel):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(String, unique=True)
    name = Column(String, index=True)
    position = Column(String, nullable=False)